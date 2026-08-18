# -*- coding: utf-8 -*-
"""Kategori içeriğini v9/v10.2 -> v11 (blog skill'i ile hizalı) taşır.

Kural: YAZARIN METNİNE DOKUNULMAZ. Yalnız görsel katman yenilenir, bölüm sırası
kapanış -> Fix CTA -> SSS olacak şekilde değişir ve FAQ Schema eklenir.

Kullanım: python3 port_kategori_v11.py <girdi.html> [<slug>]
"""
import os
import re
import sys

import os as _os
sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__))))
from category_components import *  # noqa: F401,F403
from bs4 import BeautifulSoup, NavigableString

OUT = _os.environ.get("GAMEPLUS_OUT", _os.getcwd())

# Dynamic CTA hedef rotasyonu: kategori slug'ına göre sabit ve tekrarlanabilir dağılım.
ROTASYON = ["https://gameplus.com.tr/paketler",
            "https://gameplus.com.tr/gfn",
            "https://gameplus.com.tr/geforce-now-nedir"]


def ic_html(el):
    """Öğenin iç HTML'i; yazarın <strong>/<a> biçimlemesi korunur, inline style atılır."""
    kopya = BeautifulSoup(str(el), "html.parser")
    for t in kopya.find_all(True):
        for oz in ("style", "class"):
            t.attrs.pop(oz, None)
    kok = kopya.find(el.name)
    return "".join(str(c) for c in kok.children).strip()


def duz(el):
    return re.sub(r"\s+", " ", el.get_text()).strip()


def cikar(soup):
    """Kaynak HTML'den yapıyı çıkarır."""
    v = {"tldr": [], "info": [], "tablolar": [], "notlar": [], "callout": None,
         "dyn": None, "fix": None, "faq": [], "akis": []}

    for el in soup.children:
        if getattr(el, "name", None) is None or el.name == "style":
            continue
        cls = " ".join(el.get("class", []))

        if el.name in ("h2", "h3", "h4"):
            v["akis"].append((el.name, ic_html(el)))
        elif el.name == "p":
            v["akis"].append(("p", ic_html(el)))
        elif el.name in ("ul", "ol") and "tldr" not in cls:
            maddeler = [ic_html(li) for li in el.find_all("li", recursive=False)]
            v["akis"].append((el.name, maddeler))
        elif "tldr-block" in cls:
            for li in el.find_all("li"):
                v["tldr"].append(ic_html(li))
            v["akis"].append(("tldr", None))
        elif "info-card" in cls:
            # Kaynak yapı: .gp-cell > <span>ETİKET</span><span>DEĞER</span> (span ya da div olabilir)
            for h in el.find_all("div", recursive=False):
                satirlar = [duz(x) for x in h.find_all(["span", "div", "p"]) if duz(x)]
                satirlar = [x for i, x in enumerate(satirlar) if x not in satirlar[:i]]
                if len(satirlar) >= 2:
                    v["info"].append((satirlar[0], satirlar[1]))
            v["akis"].append(("info", None))
        elif "table-wrap" in cls or el.find("table"):
            t = el.find("table")
            basliklar = [ic_html(th) for th in t.find_all("th")]
            satirlar = [[ic_html(td) for td in tr.find_all("td")]
                        for tr in t.find_all("tr") if tr.find("td")]
            v["tablolar"].append((basliklar, satirlar))
            v["akis"].append(("tablo", len(v["tablolar"]) - 1))
        elif "editor-note" in cls:
            p = el.find("p")
            v["notlar"].append(ic_html(p) if p else duz(el))
            v["akis"].append(("not", len(v["notlar"]) - 1))
        elif "callout" in cls:
            p = el.find("p")
            v["callout"] = ic_html(p) if p else duz(el)
            v["akis"].append(("callout", None))
        elif "faq-block" in cls or el.find("details"):
            for d in el.find_all("details"):
                s = d.find("summary")
                soru = re.sub(r"^\s*\+\s*", "", duz(s))
                cevap_el = d.find("p") or d.find("div")
                v["faq"].append((soru, ic_html(cevap_el) if cevap_el else ""))
            v["akis"].append(("faq", None))
        else:
            # CTA kartları: içindeki linke göre ayırt edilir
            a = el.find("a", href=True)
            if not a:
                continue
            baslik = ""
            for d in el.find_all("div"):
                t = duz(d)
                if t and len(t) < 90 and not d.find("div") and not d.find("a"):
                    baslik = t
            p = el.find("p")
            aciklama = ic_html(p) if p else ""
            if "/gfn/paketler" in a["href"]:
                v["fix"] = (baslik, aciklama)
                v["akis"].append(("fix", None))
            else:
                v["dyn"] = (baslik, aciklama)
                v["akis"].append(("dyn", None))
    return v


def kur(v, slug):
    """Yeni gövdeyi kurar; sıra kapanış -> Fix CTA -> SSS."""
    dyn_url = ROTASYON[sum(ord(c) for c in slug) % len(ROTASYON)]
    parcalar, kaynak = [], []

    # SSS bölümü ve Fix CTA akıştan çıkarılır, sona eklenir
    i_sss = next((i for i, (t, _) in enumerate(v["akis"]) if t == "faq"), None)
    sss_basligi = None
    if i_sss is not None and i_sss > 0 and v["akis"][i_sss - 1][0] == "h3":
        sss_basligi = v["akis"][i_sss - 1][1]

    atla = set()
    if i_sss is not None:
        atla.add(i_sss)
        if sss_basligi:
            atla.add(i_sss - 1)
    for i, (t, _) in enumerate(v["akis"]):
        if t == "fix":
            atla.add(i)

    for i, (t, d) in enumerate(v["akis"]):
        if i in atla:
            continue
        if t in ("h2", "h3", "h4"):
            parcalar.append(f"<{t}>{d}</{t}>")
            kaynak.append(d)
        elif t == "p":
            parcalar.append(f"<p>{d}</p>")
            kaynak.append(d)
        elif t == "ul":
            parcalar.append(render_list(d))
            kaynak.extend(d)
        elif t == "ol":
            parcalar.append("<ol>\n" + "\n".join(f"  <li>{x}</li>" for x in d) + "\n</ol>")
            kaynak.extend(d)
        elif t == "tldr":
            parcalar.append(render_tldr(v["tldr"]))
        elif t == "info":
            parcalar.append(render_info_card(v["info"]))
        elif t == "tablo":
            basliklar, satirlar = v["tablolar"][d]
            parcalar.append(render_table(basliklar, satirlar))
        elif t == "not":
            parcalar.append(render_editor_note(v["notlar"][d]))
        elif t == "callout":
            parcalar.append(render_highlight(v["callout"]))
        elif t == "dyn":
            b, a = v["dyn"]
            parcalar.append(render_category_dynamic_cta(b, a, dyn_url))

    # sona: Fix CTA -> SSS -> schema
    if v["fix"]:
        parcalar.append(render_category_fix_cta(*v["fix"]))
    if v["faq"]:
        parcalar.append(f"<h3>{sss_basligi or 'Sık Sorulan Sorular'}</h3>")
        parcalar.append(render_faq_accordion(v["faq"]))
        parcalar.append(render_faq_schema(v["faq"]))
    return "\n".join(parcalar), kaynak


def main():
    yol = sys.argv[1]
    slug = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(yol).rsplit(".", 1)[0]
    ham = open(yol, encoding="utf-8").read()
    soup = BeautifulSoup(ham, "html.parser")
    v = cikar(soup)
    body, kaynak = kur(v, slug)
    final = wrap_gp_content(CATEGORY_STYLE + "\n" + body)

    oyun_sayisi = next((dg for et, dg in v["info"] if "+" in dg), None)
    print("=== 1) Çıktı kontrolü ===")
    ok1 = print_report(verify_category_output(final, oyun_sayisi_metni=oyun_sayisi))
    print("=== 2) Yazar metni korundu mu ===")
    orij = "".join(f"<p>{x}</p>" for x in kaynak)
    ok2 = print_source_report(orij, final)
    print("=== 3) Yapı ===")
    print(f"  TLDR {len(v['tldr'])} | info {len(v['info'])} | tablo {len(v['tablolar'])} | "
          f"not {len(v['notlar'])} | FAQ {len(v['faq'])} | callout {'var' if v['callout'] else 'YOK'}")
    print(f"  dynamic CTA -> {ROTASYON[sum(ord(c) for c in slug) % len(ROTASYON)]}")

    open(os.path.join(OUT, f"kategori-v11-{slug}.txt"), "w", encoding="utf-8").write(final)
    open(os.path.join(OUT, f"onizleme-kategori-{slug}.html"), "w", encoding="utf-8").write(
        embed_fonts(PAGE_HEAD.replace("__TITLE__", slug) + final + PAGE_FOOT))
    print(f"\nboyut: {len(final)} karakter")
    print("TESLİM EDİLEBİLİR" if (ok1 and ok2) else "!!! DÜZELTME GEREKLİ !!!")


if __name__ == "__main__":
    main()

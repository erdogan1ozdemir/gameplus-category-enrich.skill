# -*- coding: utf-8 -*-
"""Kategori sayfasi bilesenleri - v11, blog skill'i ile TAM HIZALI.

Tasarim, tipografi, renk ve muhendislik blog skill'inden (gameplus_blog_components) MIRAS ALINIR;
burada yalniz kategoriye ozgu farklar tanimlanir:

  1. Conic glow YOK      -> .gp-conic animasyonu notrlestirilir, duz 1px kenarlik kalir
  2. Floating ToC YOK    -> ilgili CSS ailesi cikarilir, render edilmez
  3. H1 YOK              -> sayfa basligi grid tarafinda; govde H2 ile baslar
  4. YouTube embed YOK
  5. Onceki haftalar / oyun basligi / card-table / siralama tablosu bilesenleri YOK
  6. CTA hedefleri farkli (bkz. render_category_dynamic_cta / render_category_fix_cta)
  7. FAQ Schema (JSON-LD) EKLENIR - blogda yok

Kullanim:
    import sys; sys.path.insert(0, "<kategori-skill>/scripts")
    from category_components import *
    final = wrap_gp_content(CATEGORY_STYLE + "\\n" + body)
"""
import os
import re
import sys

# --- blog bilesen kutuphanesini bul ---
_BLOG_CANDIDATES = [
    os.environ.get("GAMEPLUS_BLOG_SKILL", ""),
    os.path.expanduser("~/.claude/skills/gameplus-blog-enrich-v2/scripts"),
    os.path.join(os.path.dirname(__file__), "..", "..", "gameplus-blog-enrich-v2", "scripts"),
]
for _c in _BLOG_CANDIDATES:
    if _c and os.path.isfile(os.path.join(_c, "gameplus_blog_components.py")):
        sys.path.insert(0, _c)
        break
else:
    raise ImportError(
        "gameplus_blog_components.py bulunamadi. Blog skill'i kurulu olmali "
        "(~/.claude/skills/gameplus-blog-enrich-v2) ya da GAMEPLUS_BLOG_SKILL yolu verilmeli."
    )

from gameplus_blog_components import (  # noqa: E402
    ANIMATED_BORDER_STYLE, SVG_SPARKLE, SVG_CHECK, SVG_DOC, SVG_BULB, SVG_EXT_LINK,
    GENRE_BADGE_COLORS, GFN_CATEGORY_URLS, badge_color_for, category_url_for,
    slugify, hex_to_rgba, lighten, inject_heading_ids, wrap_gp_content,
    render_tldr, render_info_card, render_list, render_editor_note, render_highlight,
    render_table, render_genre_tags, render_game_cell, render_faq_accordion,
    verify_source_preserved, print_source_report, print_report,
    PAGE_HEAD, PAGE_FOOT, embed_fonts,
)

# ============================================================================
# 1) CATEGORY_STYLE - blog stil blogu, kategoride kullanilmayan aileler cikarilmis
# ============================================================================

# Kategoride HIC kullanilmayan sinif aileleri. Bir kural YALNIZCA bu desenlerden
# olusuyorsa atilir; karma seciciler (ortak bir sinifla birlikte) korunur.
_KULLANILMAYAN = re.compile(
    r"floating-toc|gp-toc-|gp-toptop|"          # icindekiler
    r"gp-prev-week|gp-pw-|prev-weeks-grid|"     # onceki haftalar kartlari
    r"gp-yt-|"                                   # youtube sarmalayici
    r"gp-game-head|gp-game-name|gp-game-badge|gp-game-meta|gp-game-info-card|"
    r"gp-tg-link|gp-tg-meta|card-table|card-row|gp-name|gp-badge|"   # oyun basligi / card-table
    r"gp-table-rank|gp-col-num|gp-row-feat|"     # siralama tablosu
    r"cta-ubisoft|cta-compact|gp-cta-compact"    # ubisoft + one cikan oyun CTA'si
)


def _kurallara_bol(css):
    """CSS'i (at-rule bloklari dahil) ust duzey birimlere ayirir.
    Donen her birim ya '@media ... { ... }' butunu ya da tek bir 'secici { ... }' kuralidir."""
    birimler, tampon, derinlik = [], "", 0
    for ch in css:
        tampon += ch
        if ch == "{":
            derinlik += 1
        elif ch == "}":
            derinlik -= 1
            if derinlik == 0:
                birimler.append(tampon)
                tampon = ""
    if tampon.strip():
        birimler.append(tampon)
    return birimler


def _kural_atilir_mi(birim):
    """Secici listesindeki TUM seciciler kullanilmayan aileye aitse True."""
    i = birim.find("{")
    if i < 0:
        return False
    seciciler = [s.strip() for s in birim[:i].split(",") if s.strip()]
    if not seciciler:
        return False
    return all(_KULLANILMAYAN.search(s) for s in seciciler)


def _kategori_stili():
    ic = ANIMATED_BORDER_STYLE
    ic = ic.replace("<style>", "", 1).replace("</style>", "", 1)

    # conic animasyonunun altyapisi kategoride gereksiz
    ic = re.sub(r"@property\s+--gp-conic-angle\s*\{.*?\}", "", ic, flags=re.S)
    ic = re.sub(r"@keyframes\s+gp-conic-spin\s*\{.*?\n\}", "", ic, flags=re.S)

    cikti = []
    for birim in _kurallara_bol(ic):
        s = birim.strip()
        if not s:
            continue
        if s.startswith("@media"):
            bas = s[: s.find("{") + 1]
            govde = s[s.find("{") + 1: s.rfind("}")]
            ickurallar = [b for b in _kurallara_bol(govde) if b.strip() and not _kural_atilir_mi(b)]
            if ickurallar:
                cikti.append(bas + "".join(ickurallar) + "}")
            continue
        if _kural_atilir_mi(s):
            continue
        cikti.append(s)

    govde = "\n".join(cikti)
    govde = re.sub(r"\n{3,}", "\n\n", govde)
    return "<style>\n" + govde + "\n" + _KATEGORI_EK + "\n</style>\n"


# Kategoriye ozgu ekler. Blok EN SONDA durur, onceki kurallari bilincli ezer.
_KATEGORI_EK = """
.gp-content .gp-conic { position: relative; border-radius: 12px; padding: 0;
  border: 1px solid #29292B; background: transparent; animation: none; }
.gp-content .gp-conic::before { content: none; }
.gp-content .gp-conic-inner { background: transparent; border-radius: 11px; }
.gp-content .gp-cta-dynamic .gp-conic-inner { padding: 20px 24px; }
"""

CATEGORY_STYLE = _kategori_stili()


# ============================================================================
# 2) CTA'lar - kategoriye ozgu hedefler ve GA4 id'leri
# ============================================================================

# Sayfa-ortasi (dynamic) CTA hedefleri. /firsatlar KALDIRILDI (v11, marka karari);
# yerine GAME+ paketleri geldi. Kategoriler arasinda rotasyon yapilir.
DYNAMIC_CTA_HEDEFLERI = {
    "https://gameplus.com.tr/gfn": "GeForce NOW'u Keşfet",
    "https://gameplus.com.tr/geforce-now-nedir": "GeForce NOW Nasıl Çalışır?",
    "https://gameplus.com.tr/paketler": "GAME+ Paketleri",
}
FIX_CTA_URL = "https://gameplus.com.tr/gfn/paketler"


def render_category_dynamic_cta(headline, desc, url, label=None, eyebrow="GAME+ &bull; BULUT OYUN"):
    """Sayfa ortasi CTA. url DYNAMIC_CTA_HEDEFLERI icinden olmali:
    /gfn, /geforce-now-nedir veya /paketler. GFN paketlerine ve kategorinin kendisine GITMEZ."""
    if url not in DYNAMIC_CTA_HEDEFLERI:
        raise ValueError(
            f"Dynamic CTA hedefi gecersiz: {url}\n"
            f"Izin verilenler: {', '.join(DYNAMIC_CTA_HEDEFLERI)}"
        )
    label = label or DYNAMIC_CTA_HEDEFLERI[url]
    return f'''<div class="cta-paketler gp-cta-dynamic gp-conic">
<div class="gp-conic-inner">
  <div class="gp-cta-eyebrow"><span>{SVG_SPARKLE}{eyebrow}</span></div>
  <div class="gp-cta-title">{headline}</div>
  <p class="gp-cta-desc">{desc}</p>
  <a class="gp-btn gp-btn-solid" id="category-dynamic-cta" href="{url}">{label} &rarr;</a>
</div>
</div>
'''


def render_category_fix_cta(headline, desc, label="GeForce NOW Paketlerini İncele"):
    """Sayfa sonundaki sabit CTA. Donusumun gerceklestigi TEK paketler linki."""
    return f'''<div class="cta-end gp-conic">
<div class="gp-conic-inner">
  <div class="gp-cta-eyebrow"><span>{SVG_SPARKLE}GAME+ &bull; BULUT OYUN</span></div>
  <div class="gp-cta-title">{headline}</div>
  <p class="gp-cta-desc">{desc}</p>
  <a class="gp-btn gp-btn-solid" id="category-packages-button" href="{FIX_CTA_URL}">{label} &rarr;</a>
</div>
</div>
'''


# ============================================================================
# 3) FAQ Schema (JSON-LD)
# ============================================================================

def _duz_metin(html):
    t = re.sub(r"<[^>]+>", " ", html)
    t = (t.replace("&nbsp;", " ").replace("&amp;", "&").replace("&rarr;", "->")
          .replace("&lt;", "<").replace("&gt;", ">").replace("&bull;", "-")
          .replace("&quot;", '"').replace("&#39;", "'"))
    return re.sub(r"\s+", " ", t).strip()


def render_kategori_schema(kategori_url, ad, aciklama, guncelleme=None, kirinti=None):
    """Kategori sayfasi icin BreadcrumbList + CollectionPage JSON-LD.

    FAQPage tek basina kaliyordu; bu blok sayfa hiyerarsisini (kirinti) ve sayfanin bir
    KOLEKSIYON oldugunu makine tarafinda okunur hale getirir. `guncelleme` ISO tarih
    (YYYY-MM-DD) - tazelik sinyali icin; uydurma tarih VERILMEZ, uretim tarihi kullanilir."""
    import json
    kirinti = kirinti or [
        ("Ana Sayfa", "https://gameplus.com.tr/"),
        ("GeForce NOW", "https://gameplus.com.tr/gfn"),
        ("Oyunlar", "https://gameplus.com.tr/gfn/oyunlar"),
        (ad, kategori_url),
    ]
    koleksiyon = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": ad,
        "description": _duz_metin(aciklama),
        "url": kategori_url,
        "isPartOf": {"@type": "WebSite", "name": "GAME+",
                     "url": "https://gameplus.com.tr/"},
        "publisher": {"@type": "Organization", "name": "GAME+",
                      "url": "https://gameplus.com.tr/"},
    }
    if guncelleme:
        koleksiyon["dateModified"] = guncelleme
    ekmek = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(kirinti)
        ],
    }
    cikti = []
    for veri in (ekmek, koleksiyon):
        govde = json.dumps(veri, ensure_ascii=False, indent=2).replace("</", "<\\/")
        cikti.append(f'<script type="application/ld+json">\n{govde}\n</script>')
    return "\n".join(cikti) + "\n"


def render_faq_schema(pairs):
    """FAQPage JSON-LD. Sorular ve cevaplar GORUNEN FAQ metniyle BIREBIR ayni olmali;
    bu yuzden render_faq_accordion'a verdigin `pairs` listesinin AYNISI gecilir.

    Not: Google FAQ zengin sonucunu artik yalnizca resmi kurum ve saglik sitelerinde
    gosteriyor; isaretlemenin degeri bugun AI Overviews / GEO tarafinda."""
    import json
    veri = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": _duz_metin(q),
                "acceptedAnswer": {"@type": "Answer", "text": _duz_metin(a)},
            }
            for q, a in pairs
        ],
    }
    govde = json.dumps(veri, ensure_ascii=False, indent=2)
    # </script> kacisi: JSON icinde gecerse script blogunu erken kapatir
    govde = govde.replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{govde}\n</script>\n'


# ============================================================================
# 4) Kategori cikti dogrulamasi
# ============================================================================

def verify_category_output(final_html, expect_faq=True, oyun_sayisi_metni=None):
    """Kategori gövdesi icin zorunlu kontroller. print_report(res) ile bas; FAIL varsa TESLIM ETME."""
    r = []

    # print_report ile ayni bicim: (STATUS, ad, aciklama) uclusu
    def add(kosul, ad, iyi, kotu, warn=False):
        if kosul:
            r.append(("PASS", ad, iyi))
        else:
            r.append(("WARN" if warn else "FAIL", ad, kotu))

    govde = final_html.split("</style>")[-1]
    duz = _duz_metin(govde)

    # --- yapi ---
    add(final_html.count("<style") == 1, "Stil bloğu (1x)", "bir kez",
        f"{final_html.count('<style')} adet <style> var")
    add('class="gp-content"' in final_html, ".gp-content wrapper", "var",
        "wrap_gp_content atlanmış - hiçbir stil uygulanmaz")
    # @keyframes / @property govdeleri ('to {', 'from {', '0% {') scope kontrolune girmez
    _css = final_html.split("</style>")[0]
    _css = re.sub(r"@(?:keyframes|property)[^{]*\{(?:[^{}]|\{[^{}]*\})*\}", "", _css, flags=re.S)
    sc = re.findall(r"(?m)^\s*([.#a-zA-Z\[][^{@\n]*)\{", _css)
    kacak = [s.strip() for s in sc if ".gp-content" not in s and not s.strip().startswith("@")]
    add(not kacak, "CSS scope (.gp-content)", "tüm seçiciler scoped",
        f"scope dışı seçici: {kacak[:3]}")

    # --- kategoriye ozgu yapi kurallari ---
    add("<h1" not in govde.lower(), "H1 YOK", "yok",
        "gövdede H1 var - kategori sayfasında H1 grid tarafında, gövde H2 ile başlar")
    ilk = re.search(r"<(h[1-6])\b", govde, re.I)
    add(ilk and ilk.group(1).lower() == "h2", "İlk başlık H2", "ilk başlık H2",
        f"ilk başlık {ilk.group(1) if ilk else 'YOK'} - kategori gövdesi H2 ile başlamalı")
    add("floating-toc" not in govde, "Floating ToC yok", "yok",
        "kategori sayfasında İçindekiler kullanılmaz")
    add("youtube" not in govde.lower(), "YouTube embed yok", "yok",
        "kategori içeriğinde YouTube embed kullanılmaz")

    # --- zorunlu bilesenler ---
    add("tldr-block" in govde, "Hızlı Özet", "var", "TLDR bloğu yok")
    n_tldr = len(re.findall(r'<span class="gp-tldr-text">', govde))
    add(3 <= n_tldr <= 6, "Hızlı Özet 3-6 madde", f"{n_tldr} madde", f"{n_tldr} madde (3-6 olmalı)")
    n_cell = govde.count('class="gp-cell"')
    add('class="info-card"' in govde and n_cell == 4, "Info-card 4 metrik", f"{n_cell} metrik",
        f"info-card {n_cell} metrik içeriyor (4 olmalı; 0 ise veri çıkarımı boş dönmüş)")
    add("editor-note" in govde, "Editör Notu", "var", "Editör Notu yok")
    add("highlight-box" in govde or "Hatırlatma" in govde, "Lisans hatırlatması", "var",
        "lisans callout'u yok (zorunlu)")
    add('class="gp-list"' in govde, "Madde listesi", "var", "hiç bullet listesi yok", warn=True)
    if expect_faq:
        n_faq = govde.count("<details")
        add(4 <= n_faq <= 12, "FAQ 4-12 madde", f"{n_faq} soru",
            f"{n_faq} soru (4-12 olmalı; alt tür soruları eklendikten sonra üst sınır 12)")
        add("application/ld+json" in govde and "FAQPage" in govde, "FAQ Schema", "var",
            "FAQPage JSON-LD yok - render_faq_schema ekle")
    add("BreadcrumbList" in govde and "CollectionPage" in govde, "Kategori şeması", "var",
        "BreadcrumbList + CollectionPage JSON-LD yok - render_kategori_schema ekle", warn=True)

    # --- sira: kapanis -> CTA -> FAQ ---
    i_fix = govde.find('id="category-packages-button"')
    i_faq = govde.find("<details")
    add(i_fix > 0 and i_faq > i_fix, "Sıra: CTA -> FAQ", "doğru sırada",
        "kapanış CTA'sı FAQ'tan SONRA gelmeli değil; sıra kapanış -> CTA -> FAQ")

    # --- CTA kurallari ---
    add("firsatlar" not in govde, "Fırsatlar linki yok", "yok",
        "/firsatlar linki var - dynamic CTA /gfn, /geforce-now-nedir veya /paketler'e gider")
    dyn = re.search(r'id="category-dynamic-cta"[^>]*href="([^"]+)"', govde) or \
        re.search(r'href="([^"]+)"[^>]*id="category-dynamic-cta"', govde)
    add(dyn is not None, "Dynamic CTA", "var", "sayfa ortası CTA yok")
    if dyn:
        add(dyn.group(1) in DYNAMIC_CTA_HEDEFLERI, "Dynamic CTA hedefi",
            dyn.group(1), f"izin verilmeyen hedef: {dyn.group(1)}")
    add(govde.count('id="category-packages-button"') == 1, "Fix CTA", "var",
        "sabit CTA yok ya da birden çok")

    # --- icerik yasaklari ---
    add("—" not in govde, "Em dash yok", "yok", "em dash (—) var")
    add("PEGI" not in govde and not re.search(r"\b\d{1,2}\s*\+\s*yaş", duz), "PEGI / yaş yok", "yok",
        "PEGI ya da yaş önerisi var")
    add("Steam Workshop" not in govde, "Steam Workshop yok", "yok", "Steam Workshop iddiası var")
    add("<!--" not in final_html and "/*" not in final_html, "Çıktıda yorum yok", "yorum yok",
        "HTML/CSS yorumu var - CMS'e giden çıktıda yorum bulunmaz")
    add("data:font" not in final_html, "Gömülü font yok", "yok",
        "gövdede base64 font var - LİSANS İHLALİ")
    add("onclick=" not in final_html, "Inline onclick yok", "yok", "inline onclick var")
    if oyun_sayisi_metni:
        add(re.search(r"\d+\+", oyun_sayisi_metni) is not None, "Yuvarlanmış oyun sayısı",
            oyun_sayisi_metni, f"'{oyun_sayisi_metni}' yuvarlanmış 'X+' biçiminde değil")

    # --- etiket dengesi ---
    dengesiz = []
    for t in ("div", "table", "tbody", "tr", "td", "th", "p", "details", "style", "ul", "li"):
        ac = len(re.findall(r"<" + t + r"[\s>]", final_html))
        kap = len(re.findall(r"</" + t + r">", final_html))
        if ac != kap:
            dengesiz.append(f"{t}: {ac}/{kap}")
    add(not dengesiz, "Etiket dengesi", "tüm etiketler dengeli", f"dengesiz: {dengesiz}")

    return r

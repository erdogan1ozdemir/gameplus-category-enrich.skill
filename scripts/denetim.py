# -*- coding: utf-8 -*-
"""kategori-icerikleri/*.txt ciktilarinin yapisal denetimi: tablo, TLDR, CTA, SSS, schema, yazim, Kural 21."""
import io, os, re, json, sys
from bs4 import BeautifulSoup
D = sys.argv[1] if len(sys.argv) > 1 else "kategori-icerikleri"
sorun, ozet = [], []
for f in sorted(os.listdir(D)):
    if not f.endswith(".txt"): continue
    slug = f[12:-4]; html = io.open(f"{D}/{f}", encoding="utf-8").read(); g = html.split("</style>")[-1]
    s = BeautifulSoup(g, "html.parser")
    for k, t in enumerate(s.find_all("table"), 1):
        th = len(t.find_all("th")); satir = [len(tr.find_all(["td", "th"])) for tr in t.find_all("tr")]
        if any(x != th for x in satir) or t.find("table") or t.find(["h2", "h3", "h4"]):
            sorun.append(f"{slug} tablo{k}: th={th} satırlar={satir}")
    tl = s.select("[class*=tldr] li")
    if not (3 <= len(tl) <= 6) or any(not x.get_text(strip=True) for x in tl): sorun.append(f"{slug} TLDR madde={len(tl)}")
    ts = [re.sub(r"<[^>]+>", "", t).strip() for t in re.findall(r'<div class="gp-cta-title">(.*?)</div>', g, re.S)]
    ds = [re.sub(r"<[^>]+>", "", t).strip() for t in re.findall(r'<p class="gp-cta-desc">(.*?)</p>', g, re.S)]
    if len(ts) != 2 or len(ds) != 2: sorun.append(f"{slug} CTA sayısı başlık={len(ts)} açıklama={len(ds)}")
    for t in ts:
        if not t or t == "None" or t.isupper() or len(t) < 10 or "PERFORMANCE" in t.upper().replace(" ", "")[:11]: sorun.append(f"{slug} CTA başlığı: '{t}'")
    for d in ds:
        if not d or d == "None" or len(d) < 30: sorun.append(f"{slug} CTA açıklaması: '{d[:40]}'")
    for a in s.select("#category-dynamic-cta, #category-packages-button"):
        if "/firsatlar" in a["href"] or a["href"].rstrip("/").endswith("/gfn"): sorun.append(f"{slug} CTA hedef {a['href']}")
    det = s.find_all("details"); sorular = [re.sub(r"^\s*\+\s*", "", d.find("summary").get_text(strip=True)) for d in det]
    if not (4 <= len(det) <= 12): sorun.append(f"{slug} FAQ={len(det)}")
    for d in det:
        cev = d.get_text(" ", strip=True).replace(d.find("summary").get_text(" ", strip=True), "", 1).strip()
        if len(cev) < 40: sorun.append(f"{slug} kısa FAQ cevabı: {sorular[det.index(d)][:50]}")
    sem = 0
    for sc in s.find_all("script", type="application/ld+json"):
        try: j = json.loads(sc.string); sem += 1
        except Exception as e: sorun.append(f"{slug} schema JSON hatası: {e}"); continue
        if j.get("@type") == "FAQPage" and [q["name"] for q in j["mainEntity"]] != sorular: sorun.append(f"{slug} FAQ schema soru uyumsuz")
    if sem < 2: sorun.append(f"{slug} schema sayısı {sem}")
    txt = re.sub(r"<script.*?</script>", "", g, flags=re.S); txt = re.sub(r"<[^>]+>", " ", txt)
    if "İndie" in html: sorun.append(f"{slug} İndie kaldı x{html.count('İndie')}")
    for m in re.finditer(r"(?<![\w/.-])(arcade|indie)(?!\w)", txt): sorun.append(f"{slug} küçük harf: {txt[max(0,m.start()-30):m.end()+10]!r}")
    if re.search(r"/oyunlar/[a-z-]*(Arcade|Indie)", html): sorun.append(f"{slug} URL bozuldu")
    for m in re.finditer(r"\w+(ını|ini|larını|lerini)\s+[Nn]asıl\s+\w+n[ıiuü]r", txt): sorun.append(f"{slug} dilbilgisi: {m.group(0)}")
    for a in s.find_all("a", href=True):
        h = a["href"]; rel = a.get("rel") or []
        if h.startswith("#"): continue
        dis = not (h.startswith("/") or "gameplus.com.tr" in h)
        if a.get("target") != "_blank": sorun.append(f"{slug} target yok: {h}")
        if dis and "nofollow" not in rel: sorun.append(f"{slug} nofollow yok: {h}")
        if not dis and "nofollow" in rel: sorun.append(f"{slug} iç linkte nofollow: {h}")
        if "firsatlar" in h: sorun.append(f"{slug} fırsatlar linki: {h}")
    kok = BeautifulSoup(html, "html.parser").select_one(".gp-content")
    dom = len([c for c in kok.children if getattr(c, "name", None)]) if kok else -1
    if dom > 60 or dom < 0: sorun.append(f"{slug} DOM genişliği {dom}")
    ozet.append(f"{slug:18s} tablo {len(s.find_all('table'))} tldr {len(tl)} faq {len(det):2d} schema {sem} dom {dom:2d} | dyn='{ts[0][:36] if ts else '-'}' | fix='{ts[1][:30] if len(ts)>1 else '-'}'")
print("\n".join(ozet)); print(f"\n=== SORUN ({len(sorun)}) ==="); print("\n".join(sorun) or "yok")
sys.exit(1 if sorun else 0)

# -*- coding: utf-8 -*-
"""Kategori içeriğini v9 (yeşil, layered frame) -> v10.2 "Game+ UI" (sarı, Figma kart) taşır.

Kural: METNE DOKUNMAZ. Sadece görsel katman + GA4 id'leri. Kategori kuralı gereği
conic glow ve floating ToC EKLENMEZ.
Kullanım: python3 port_category_v10.py <v9-out/xxx-icerik-v9.html> [<çıktı.html>]
"""
import re, sys, os
# Editör Notu / Hatırlatma yapısı BLOG ile birebir aynı olmalı -> bileşenleri doğrudan blog skill'inden al.
# Blog skill'i birkaç olası konumdan aranır (kurulu skill dizini / kardeş klasör / env override).
_BLOG_CANDIDATES = [
    os.environ.get("GAMEPLUS_BLOG_SKILL", ""),
    os.path.expanduser("~/.claude/skills/gameplus-blog-enrich-v2/scripts"),
    os.path.join(os.path.dirname(__file__), "..", "..", "gameplus-blog-enrich-v2", "scripts"),
]
for _c in _BLOG_CANDIDATES:
    if _c and os.path.isfile(os.path.join(_c, "gameplus_blog_components.py")):
        sys.path.insert(0, _c); break
from gameplus_blog_components import render_editor_note, render_highlight

NS = "font-family:'New Science',GreycliffCF,-apple-system,sans-serif;"

# ---- v10.2 kategori style bloğu (conic YOK, ToC YOK) ----
STYLE_V10 = """<style>
/* Game+ UI v10.2 — kategori (conic glow ve floating ToC KULLANILMAZ) */
@keyframes gp-pulse-plus { 0%,100%{transform:scale(1);opacity:1;} 50%{transform:scale(1.18);opacity:0.85;} }
.gp-card { border:1px solid #29292B; border-radius:16px; background:#161616; }
.gp-cell { background:#0D0D0D; border:1px solid #29292B; border-radius:12px; padding:20px; text-align:center; }
.tldr-block strong { color:#fff; }
.editor-note p { color:#fff !important; margin:0; line-height:1.5; }
.callout p { color:#fff !important; margin:0; line-height:1.5; }
.gp-table-wrap { background:#161616; border:1px solid #29292B; border-radius:16px; overflow:hidden; margin:24px 0; }
.gp-table-wrap table { width:100%; border-collapse:collapse; background:transparent; }
.gp-table-wrap tbody tr { transition:background 0.15s ease; }
.gp-table-wrap tbody tr:hover > td { background:rgba(255,201,0,0.07) !important; }
.gp-table-wrap tbody tr:hover > td:first-child { color:#FFC900 !important; }
.gp-table-wrap tbody tr:last-child td { border-bottom:none !important; }
.gp-table-wrap td strong { color:#fff; }
.faq-a p { color:#B2B2B2 !important; line-height:1.6; }
.faq-item .faq-icon { animation: gp-pulse-plus 2.2s ease-in-out infinite; display:inline-flex; align-items:center; justify-content:center; width:22px; height:22px; flex-shrink:0; color:#FFC900; font-size:1.5em; font-weight:300; line-height:1; }
.faq-item[open] .faq-icon { transform:rotate(45deg); color:#FFC900; }
.faq-item summary::-webkit-details-marker { display:none; }
.faq-item summary::marker { display:none; }
.gp-btn:hover { filter:brightness(1.08); }
/* Gövde madde listeleri: nokta rengi Hızlı Özet bullet'ı ile aynı (#FFC900) */
ul li::marker { color:#FFC900; }
ul li { padding-left:4px; }
@media (max-width:700px){
  .gp-table-wrap > div { overflow-x:visible !important; }
  .gp-table-wrap table { font-size:0.76em !important; table-layout:fixed; width:100% !important; }
  .gp-table-wrap th, .gp-table-wrap td { padding:10px 7px !important; white-space:normal !important; overflow-wrap:break-word; vertical-align:middle !important; line-height:1.4 !important; }
  .gp-table-wrap th { text-align:center !important; letter-spacing:0.04em !important; }
  .gp-table-wrap td { text-align:left; }
}
</style>"""

SVG_DOC = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFC900" stroke-width="2.2" '
           'stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;margin-right:8px;">'
           '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>')
SVG_BULB = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFC900" stroke-width="2.2" '
            'stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;margin-right:8px;">'
            '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M15.09 14a5 5 0 1 0-6.18 0c.66.49 1.09 1.27 1.09 2.1V17h4v-.9c0-.83.43-1.61 1.09-2.1z"/></svg>')
SVG_SPARKLE = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="#FFC900" style="flex-shrink:0;margin-right:6px;'
               'vertical-align:-2px;"><path d="M12 1.5c.3 4.6 2.4 7.4 6.9 8.2.7.1.7 1.1 0 1.2-4.5.8-6.6 3.6-6.9 8.2 0 .8-1.1.8-1.2 0'
               '-.3-4.6-2.4-7.4-6.9-8.2-.7-.1-.7-1.1 0-1.2 4.5-.8 6.6-3.6 6.9-8.2.1-.8 1.2-.8 1.2 0z"/></svg>')


# Editör Notu / callout gövdesi: eyebrow div'inden SONRAKİ <p> veya <div> içeriği
_RE_GOVDE = re.compile(r'</svg>[^<]*</div>\s*<(?:p|div)[^>]*>(.*?)</(?:p|div)>\s*</div>\s*$', re.S)


def port(src: str) -> str:
    s = src
    rep = []

    def sub(pat, new, label, flags=0, expect=None):
        nonlocal s
        s2, n = re.subn(pat, new, s, flags=flags)
        if expect is not None:
            assert n == expect, f"{label}: beklenen {expect}, bulunan {n}"
        else:
            assert n > 0, f"{label}: eşleşme yok"
        s = s2
        rep.append(f"{label}: {n}")

    # 1) style bloğu
    sub(r'<style>.*?</style>', lambda m: STYLE_V10, 'style bloğu', re.S, 1)

    # 2) TLDR başlığı (yeşil -> New Science beyaz + sarı doküman ikonu)
    sub(r'<h3 style="margin:0 0 12px 0;font-size:1\.05em;font-weight:800;display:flex;align-items:center;gap:8px;color:#76b900;">.*?<span style="color:#fff;">Hızlı Özet</span></h3>',
        lambda m: (f'<h3 style="margin:0 0 14px 0;{NS}font-size:24px;line-height:32px;font-weight:600;'
                   f'color:#fff;display:flex;align-items:center;">{SVG_DOC}Hızlı Özet</h3>'),
        'TLDR başlığı', re.S, 1)

    # 2b) TLDR maddeleri: ✓ SVG -> Figma'daki sarı • (bullet)
    sub(r'<li style="display:flex;gap:11px;margin:8px 0;align-items:flex-start;line-height:1\.5;list-style:none;">'
        r'<svg width="16" height="16"[^>]*>\s*<polyline points="20 6 9 17 4 12"/>\s*</svg>',
        '<li style="display:flex;gap:10px;margin:0 0 14px;align-items:flex-start;list-style:none;">'
        '<span style="color:#FFC900;font-weight:700;font-size:16px;line-height:24px;flex-shrink:0;">&bull;</span>',
        'TLDR ✓ -> sarı bullet', re.S)

    # 3) Editör Notu ve Lisans callout: BLOG ile BİREBİR aynı yapı.
    #    (Eskiden border-left kullanılıyordu; kartın yuvarlak köşesinde "parantez" gibi görünüyordu.
    #     Blog yapısı: flex + align-items:stretch + ayrı 4px yuvarlak uçlu bar div'i.)
    def _ic_metin(html):
        """Bloğun gövde metnini (eyebrow hariç) döndürür; iç HTML etiketleri korunur."""
        m = _RE_GOVDE.search(html)
        assert m, "callout gövdesi bulunamadı"
        return m.group(1).strip()

    def rebuild_note(m):
        return render_editor_note(_ic_metin(m.group(0)))

    def rebuild_callout(m):
        return render_highlight(_ic_metin(m.group(0)))

    sub(r'<div class="editor-note gp-layer".*?</p>\s*</div>', rebuild_note, 'Editör Notu (blog yapısı)', re.S)
    sub(r'<div class="callout gp-layer".*?</div>\s*</div>', rebuild_callout, 'Lisans callout (blog yapısı)', re.S)

    #    TLDR: #161616 kart
    sub(r'<div class="tldr-block gp-layer" style="--gp-frame:rgba\(118,185,0,0\.30\);[^"]*">',
        '<div class="tldr-block gp-card" style="padding:24px;margin:24px 0;">',
        'TLDR kutusu')
    #    kalan gp-layer -> gp-card
    s = re.sub(r'class="([^"]*?)gp-layer"', r'class="\1gp-card"', s)
    s = re.sub(r'--gp-frame:rgba\([^)]*\);', '', s)

    # 6) info-card hücresi: ETİKET üstte/DEĞER altta -> DEĞER üstte (New Science sarı) / etiket altta
    def flip_cell(m):
        label, value = m.group(1), m.group(2)
        return (f'<div class="gp-cell">\n'
                f'    <div style="{NS}font-weight:600;font-size:24px;line-height:32px;color:#FFC900;'
                f'margin-bottom:6px;overflow-wrap:break-word;">{value}</div>\n'
                f'    <div style="color:#B2B2B2;font-size:16px;line-height:24px;font-weight:500;">{label}</div>\n'
                f'  </div>')
    sub(r'<div class="gp-cell">\s*<span style="display:block;font-size:0\.62em;color:#76b900;[^"]*">(.*?)</span>\s*<span style="font-size:1\.05em;font-weight:700;color:#fff;">(.*?)</span>\s*</div>',
        flip_cell, 'info-card hücreleri (değer üste)', re.S)

    # 7) Tablo başlıkları: sarı, ortalı, 16px
    sub(r'<th style="padding:12px 18px;text-align:left;border-bottom:1px solid rgba\(118,185,0,0\.18\);font-weight:800;color:#76b900;font-size:0\.65em;letter-spacing:0\.16em;text-transform:uppercase;">',
        '<th style="background:#1E1E18;padding:19px 24px;text-align:center;border-bottom:1px solid rgba(255,201,0,0.3);font-weight:700;color:#FFC900;font-size:16px;line-height:20px;">',
        'tablo başlıkları')

    # 8) CTA butonları: sarı zemin + koyu metin + GA4 id
    def btn(m):
        url, inner = m.group(1), m.group(2)
        cid = 'category-packages-button' if '/gfn/paketler' in url else 'category-dynamic-cta'
        return (f'<a id="{cid}" class="gp-btn" href="{url}" style="display:inline-flex;align-items:center;'
                f'justify-content:center;background:#FFC900;color:#131313;padding:12px 16px;border-radius:8px;'
                f'font-weight:700;font-size:16px;line-height:20px;text-decoration:none;">{inner}</a>')
    sub(r'<a href="(https://gameplus\.com\.tr[^"]*)" style="display:inline-block;background:#76b900;color:#fff;[^"]*">(.*?)</a>',
        btn, 'CTA butonları (+GA4 id)', re.S)

    # 9) Global token swap
    for a, b, lbl in [
        (r'#76b900', '#FFC900', 'yeşil->sarı'),
        (r'rgba\(118,\s*185,\s*0,', 'rgba(255,201,0,', 'yeşil rgba->sarı'),
        (r'#cbd5e1', '#B2B2B2', 'gövde gri'),
        (r'#f3f4f6', '#ffffff', 'vurgu beyaz'),
        (r'#fbbf24', '#FFC900', 'amber->sarı'),
        (r'#fde68a', '#B2B2B2', 'callout metni'),
        (r'#93c5fd', '#FFC900', 'mavi->sarı'),
        (r'#1f1f1f', '#29292B', 'ayraç'),
    ]:
        s2, n = re.subn(a, b, s)
        if n: rep.append(f"{lbl}: {n}")
        s = s2

    # 10) Başlıklar New Science (CMS kendi stilini verir; bu sadece güvenlik ağı)
    s = STYLE_V10.replace('</style>',
        f"h2,h3,h4 {{ {NS} font-weight:600; color:#fff; }}\n</style>") + s[len(STYLE_V10):]

    print("  " + " | ".join(rep))
    return s


if __name__ == '__main__':
    src_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else src_path.replace('-v9.html', '-v10.html').replace('v9-out/', 'v10-out/')
    os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)
    src = open(src_path, encoding='utf-8').read()
    out = port(src)

    # ---- KONTROL NOKTALARI ----
    from collections import Counter
    txt = lambda h: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<style>.*?</style>', '', h, flags=re.S))).split()
    # Türkçe-güvenli normalize (Editör -> EDITÖR vs EDİTÖR farkını yut); eyebrow'lar büyük harfe çevrildi
    def norm(ws):
        return Counter(w.replace('İ', 'I').replace('ı', 'i').upper() for w in ws)
    a, b = txt(src), txt(out)
    # ✓ SVG (tag) -> &bull; (entity) dönüşümü: bullet dekoratif işaret, metin değil -> karşılaştırmadan düş
    b = [w for w in b if w != '&bull;']
    da, db = norm(a), norm(b)
    eksik, fazla = da - db, db - da
    assert not eksik and not fazla, f"METİN DEĞİŞTİ!\n  kaybolan: {list(eksik.elements())[:12]}\n  eklenen: {list(fazla.elements())[:12]}"
    # Not: info-card hücrelerinde DEĞER etiketin üstüne alındı (v10.2 tasarımı) -> kelime sırası bilinçli değişti,
    # kelime kümesi birebir aynı kalır; bu yüzden sıra-duyarsız (Counter) karşılaştırma kullanılıyor.
    assert '#76b900' not in out and 'rgba(118,185,0' not in out, "yeşil kalıntı var"
    # kategori kuralı: conic glow ve floating ToC kullanılmaz (yorum metni değil, gerçek kullanım aranır)
    kod = re.sub(r'/\*.*?\*/', '', out, flags=re.S)
    assert 'gp-conic' not in kod, "kategori kuralı ihlali: conic glow eklenmiş"
    assert 'floating-toc' not in kod, "kategori kuralı ihlali: floating ToC eklenmiş"
    assert '{{' not in out and '}}' not in out, "CSS parantez kaçışı"
    assert out.count('<style>') == 1, "style bloğu 1 kez olmalı"
    assert 'category-packages-button' in out, "Fix CTA id yok"
    open(out_path, 'w', encoding='utf-8').write(out)
    print(f"  ✓ metin birebir korundu ({len(a)} kelime) | yeşil kalıntı: 0 | -> {out_path}")

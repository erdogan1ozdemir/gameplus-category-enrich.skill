# Kategori Tasarım Sistemi — v10.2 "Game+ UI" (Figma tabanlı)

Blog skill'iyle (`gameplus-blog-enrich-v2`) **aynı görsel dil**. Tek fark: kategoride **dönen conic glow ve floating İçindekiler KULLANILMAZ** (kategori metni oyun grid'inin altında durur, sade kalır).

> **v9'dan geçiş:** Eski yeşil (#76b900) + "Layered Frame" dili bırakıldı. Mevcut v9 içeriklerini taşımak için `scripts/port_category_v10.py` kullan (metne dokunmaz, yalnız görsel katman + GA4 id'leri).

## Renkler

| Token | Değer | Kullanım |
|---|---|---|
| Vurgu | `#FFC900` | başlık ikonları, eyebrow, tablo sütun başlığı, bullet, butonlar |
| Buton üzeri metin | `#131313` | dolu sarı butonların yazısı (beyaz DEĞİL) |
| Kart | `#161616` + `#29292B` kenarlık, r16 | TLDR, tablolar, CTA kartı (`.gp-card`) |
| Stat kartı | `#0D0D0D` + `#29292B`, r12 | info-card hücreleri (`.gp-cell`) |
| Tablo başlık satırı | `#1E1E18` + altında `rgba(255,201,0,0.3)` | thead |
| Ayraç | `#29292B` | satır ayraçları, kenarlıklar |
| İkincil metin | `#B2B2B2` | gövde, tablo hücreleri |
| Editör Notu zemini | `rgba(255,201,0,0.06)` | + 4px sarı bar |
| Lisans callout zemini | `rgba(255,255,255,0.04)` | + 4px sarı bar (sarı marka rengi olduğu için Editör Notu'ndan bilinçle ayrışır) |
| Hover satır | `rgba(255,201,0,0.07)` + ad `#FFC900` | tablo satırı yalnız hover'da vurgulanır |

## Tipografi
- Başlıklar (H2/H3/H4) **New Science SemiBold Extended**; gövde Greycliff CF.
- TLDR başlığı 24/32 beyaz + sarı doküman ikonu. Stat değeri 24/32 **sarı**, ortalı.
- Tablo hücresi 16/20 `#B2B2B2`; sütun başlığı Bold **`#FFC900`, ORTALI** (mobilde de ortalı).

## Bileşenler

### Editör Notu / Lisans callout — blog ile BİREBİR
`border-left` KULLANMA. Kartın yuvarlak köşesinde çizgi "parantez" gibi görünür. Doğru yapı: flex + `align-items:stretch` + **ayrı 4px yuvarlak uçlu bar div'i**:

```html
<div class="editor-note" style="background:rgba(255,201,0,0.06);border-radius:12px;padding:18px 24px 18px 20px;margin:24px 0;display:flex;gap:16px;align-items:stretch;">
  <div style="width:4px;border-radius:2px;background:#FFC900;flex-shrink:0;"></div>
  <div>
    <div style="color:#FFC900;font-size:12px;line-height:16px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;display:flex;align-items:center;">[ikon]GAME+ EDİTÖR NOTU</div>
    <p style="margin:0;color:#fff;font-size:1em;line-height:1.5;">…</p>
  </div>
</div>
```
Lisans callout aynı yapı, zemin `rgba(255,255,255,0.04)`, eyebrow `HATIRLATMA` + ampul ikonu.
**Kaynak:** blog skill'inin `render_editor_note()` / `render_highlight()` fonksiyonları. Elle yazmak yerine oradan üret — yapı birebir aynı kalsın.

### TLDR
`#161616` kart (r16) + New Science 24/32 başlık + sarı doküman ikonu; maddeler **sarı `•`** + `#B2B2B2` metin (✓ tik KULLANILMAZ). 3-6 madde.

### Info-card (stat kartları)
`#0D0D0D` kart, içerik **ortalı**, **DEĞER ÜSTTE** (New Science 24px sarı), etiket altta gri 16/24. Değer sayı olmak zorunda değil; kısa metin/insight da olabilir (<=22 karakter).

### Tablolar
`.gp-table-wrap` = `#161616` + `#29292B` + r16. thead `#1E1E18`, sarı ortalı başlıklar. Satır vurgusu yalnız hover'da.

### Madde listeleri
Gövde `<ul>` nokta rengi Hızlı Özet bullet'ı ile aynı: `ul li::marker { color:#FFC900; }`.

### CTA'lar
Dolu sarı zemin + `#131313` metin, r8. GA4 id'leri zorunlu (bkz. `ga4-tracking.md`).

## Yasak
- `gp-conic` (dönen glow) ve `floating-toc` — kategori sayfasında kullanılmaz.
- `border-left` ile callout barı.
- Yeşil `#76b900` ve türevleri (`rgba(118,185,0,*)`).

## v10.3 (blog ile hizalandı)
- **Başlık ölçekleri:** H2 22/28 (mobil 17), H3 18.5/25 (mobil 15), H4 15.5/21 (mobil 14). Gövde 16/24 (mobil 15/22).
- **"Hızlı Özet" başlığı `<div>`** (heading değil — SEO); boyut 19 (mobil 16).
- **Tablolar mobilde:** başlık satırı KALIR (thead görünür), hücreler dikey ortalı, içerik responsive; 3 sütunlu tablo düzeni (oyun adı 14/13, platform 11/10 + ok nowrap, tür ortalı) `:first-child:nth-last-child(3)` ile scoped.
- **gp-cell / info-card** mobilde 2 kolon `minmax(0,1fr)`, yazılar küçülür; **CTA butonu (`gp-btn`) mobilde 15px**.
- **Yumuşak kaydırma** (`scroll-behavior:smooth`); scroll-reveal JS yok (kategori kuralı: conic/ToC de yok).

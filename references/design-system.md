# Kategori Tasarım Sistemi — v11 (blog skill'i ile TAM HİZALI)

> **Tek kaynak:** Tipografi, renk, bileşen görünümü ve mühendislik kuralları için
> **blog skill'inin `references/design-system.md`** dosyası esastır. O dosya ne diyorsa kategori de
> onu uygular. Bu doküman yalnızca **kategoriye özgü farkları** listeler.
>
> Uygulama katmanı: `scripts/category_components.py`. Bileşenler blog kütüphanesinden **miras
> alınır**; kategoride ayrı bir tipografi, renk ya da kart tanımı YOKTUR. Elle inline stil yazma.

## Neden bu değişti

v10.2/v10.3 sürümünde kategori, blog'un **v10.3**'üne hizalıydı ve o tarihten sonra blog dokuz sürüm
ilerledi (v10.4 → v10.13). Aradaki fark tipografide üç kat başlık ölçeği, mühendislikte ise CSS
izolasyonu ve otomatik doğrulama seviyesindeydi. v11 bu açığı kapatır: kategori artık kendi CSS'ini
taşımaz, blog stil bloğunu süzerek kullanır.

## Miras alınanlar (kategoride ayrıca tanımlanmaz)

- **Tipografi**, masaüstü ve mobil: H2 32/40 (mobil 21/28) · H3 28/36 (19/26) · H4 24/32 (17/24) ·
  gövde 16/24 · Hızlı Özet başlığı 24/32 (20/24) · stat değeri 27/35 (17/23) · stat etiketi 16/24
  (13/17) · Editör Notu ve Hatırlatma 16/22 (15/22) · CTA başlığı 32/40 (19/25) · CTA metni 16/20 ·
  buton 16/20 · tablo 16/20 · küçük metin 12/16.
- **Renkler:** vurgu `#FFC900`, kart `#161616`, stat `#0D0D0D`, tablo başlık satırı `#1E1E18`,
  ayraç `#29292B`, ikincil metin `#B2B2B2`, buton üzeri `#131313`.
- **Kart arka planları şeffaftır** (blog v10.4). Kategoride de dolu zemin kullanılmaz.
- **Tablolar:** sütun başlıkları SOLA YASLI ve sarı; hücreler 16/20; oyun adı beyaz, bold değil;
  satır vurgusu yalnız hover'da; mobilde tablo sıkıştırılmaz, **yana kaydırılır** ve kabın ÜSTÜNDE
  "Tabloyu yana kaydır →" ipucu çıkar; kaydırma çubuğu her genişlikte gizlidir.
- **İstatistik kartları** yatayda ve dikeyde ortalıdır (blog v10.12).
- **Hızlı Özet madde işareti SARI `•`** (`gp-tldr-bullet`, `#FFC900`). Blogda da aynıdır; tik
  kullanılmaz.
- **Editör Notu / Hatırlatma** yapısı blog ile birebir: flex + ayrı 4px yuvarlak uçlu bar div'i.
  `border-left` KULLANMA (yuvarlak köşede parantez gibi görünür).
- **Mühendislik:** tek `<style>` bloğu, tüm seçiciler `.gp-content` önekli, sınıf tabanlı bileşenler
  (inline stil yok), çıktıda CSS/JS/HTML yorumu yok, inline `onclick` yok.

## Kategoriye özgü farklar

| # | Fark | Nasıl uygulanır |
|---|---|---|
| 1 | **Conic glow YOK** | `.gp-conic` animasyonu nötrleştirilir: `padding:1px` + `background:#29292B` + `::before{content:none}`. Kart yapısı ve iç boşluklar blogla aynı kalır, yalnız dönen ışık gider. |
| 2 | **Floating İçindekiler YOK** | CSS ailesi `CATEGORY_STYLE` üretilirken çıkarılır; `render_floating_toc` çağrılmaz. |
| 3 | **H1 YOK** | Sayfa H1'i oyun grid'i tarafında. Gövde **H2 ile başlar**, bölümler H3/H4. `ensure_leading_h1` KULLANILMAZ. |
| 4 | **YouTube embed YOK** | Kategori içeriğinde video kullanılmaz. |
| 5 | **Oyun başlığı / card-table / sıralama tablosu / önceki haftalar / Ubisoft CTA / öne çıkan oyun CTA YOK** | İlgili CSS aileleri süzülür; bileşenler çağrılmaz. |
| 6 | **CTA hedefleri farklı** | bkz. `cta-templates.md`. Dynamic CTA `/gfn`, `/geforce-now-nedir` veya `/paketler`; Fix CTA `/gfn/paketler`. |
| 7 | **FAQ Schema VAR** | `render_faq_schema(pairs)` ile `FAQPage` JSON-LD basılır. Blogda yoktur. |
| 8 | **Bölüm sırası sonu farklı** | Kapanış → Fix CTA → SSS. bkz. `structure-template.md`. |

## `CATEGORY_STYLE`

`category_components.py`, blog `ANIMATED_BORDER_STYLE`'ını alır ve **yalnızca seçicilerinin tamamı
kategoride kullanılmayan sınıflardan oluşan kuralları** atar; karma seçiciler (ortak bir sınıfla
birlikte yazılmış olanlar) korunur. Ardından kategoriye özgü ek blok en sona eklenir.

Sonuç: **37.351 → 25.927 karakter** (~11.400 karakter tasarruf). Bu, Google Sheets'in 50.000
karakterlik hücre sınırı için önemlidir.

Yeni bir kural gerekiyorsa `_KATEGORI_EK` bloğuna yaz; blok en sonda durduğu için önceki kuralları
bilinçle ezer.

## Yasak

- Yeşil `#76b900` ve türevleri.
- Office/Tailwind artığı renkler (`#CBD5E1`, `#0f172a` vb.).
- `em` bazlı punto (host sayfanın puntosuna göre kayar) — her ölçü `px`.
- Inline stil (dinamik değerler hariç), `!important`, gövdeye gömülü font.

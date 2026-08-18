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

## Port sırasında yakalanan kaynak tuzakları (v11 saha notları)

Eski içerik iki farklı nesilden geliyor ve yapıları ayrışıyor. `port_category_v11.py` bunları
otomatik ele alır; yeni bir kaynak eklerken aynı tuzaklara dikkat et:

| Tuzak | Belirti | Çözüm |
|---|---|---|
| **info-card sırası nesle göre ters** | v9'da ETİKET üstte, v10.2'de DEĞER üstte | Hücrenin ilk çocuğunun stiline bakılır: `#FFC900` / `font-size:24px` / `1.7em` varsa değer üstte, `text-transform:uppercase` varsa etiket üstte |
| **CTA'lar href'e göre ayrılamaz** | Eski içerikte HER İKİ CTA da `/gfn/paketler`e gidiyor | Sıraya göre: SON kart Fix CTA, ilk kart dynamic CTA |
| **C4 "stat banner" CTA'sında kopya yok** | Kartta yalnız sayı + etiket çiftleri ve buton var | Yaprak div'lerden istatistik şeridi elenir (`font-size:1.7em`, `font-weight:800`, `text-transform:uppercase`); kopya çıkmazsa `DYN_CTA_METNI` yedeği kullanılır |
| **Etiket metne gömülü** | Paragraf `ℹ Hatırlatma ...` / `📝 Game+ Editör Notu ...` ile başlıyor, bileşen etiketi zaten basıyor | `onek_temizle()` ile önek atılır |
| **`<details>` sarmalayıcısız** | v10.2 kaynağında SSS öğeleri üst düzeyde | `el.name == "details"` dalı |
| **Lisans callout'u `.highlight-box`** | v10.2 sınıf adı farklı | İki sınıf da callout sayılır |
| **Zorunlu bileşen kaynakta yok** | Lisans hatırlatması ya da sayfa-ortası CTA hiç yok | `LISANS_METNI` ve `DYN_CTA_METNI` yedekleri devreye girer |
| **Ham oyun sayısı** | "434 Oyun", "921 yapım" | `sayilari_yuvarla()`: >=100 en yakın 100 aşağı, <100 en yakın 10 aşağı; gövdedeki aynı sayı da güncellenir |
| **Kaynaktan gelen dizgi hatası** | Nokta sonrası boşluk yok, yarım cümle | `dizgi_duzelt()` |

**FAQ sorularında kategori bağlamı (v11 kuralı):** soru tek başına okunduğunda hangi kategoriye ait
olduğu anlaşılmalı. "Klavye-fare mı, gamepad mi tercih edilmeli?" yerine "**FPS oyunlarında**
klavye-fare mı, gamepad mi tercih edilmeli?". Oyun adı geçen ya da kategorinin kendi terimini taşıyan
sorulara DOKUNULMAZ. Revizeler `FAQ_SORU_REVIZE` haritasında tutulur; FAQ Schema **görünen soruyla**
birebir üretilir.

# HTML Structure Template (Bölüm Sırası + İçerik)

> **Not:** Bu dosya SADECE bölüm sırası ve içerik kuralları içindir. **Görünümü `design-system-v10.md` belirler** (v10.2 "Game+ UI", sarı). Buradaki snippet renkleri bağlayıcı değildir.

Section order **fixed** — don't reorder. The CMS pastes this body HTML as-is.

> ## ⚠ GÖRSEL STİL: v9 KOYU TEMA KULLAN
> Aşağıdaki snippet'ler **eski açık tema** (`#fff`, `#161616`, `#eef6ff` vb.) referans amaçlıdır. **Görsel stil için `references/design-system-v9.md`'deki KOYU v9 sürümlerini kullan** (saf siyah `#000` zemin, V9 Layered Frame, yeşil ✓ TLDR, premium info-card, zebra tablolar, nabız atan FAQ `+`). Bu dosyadan sadece **bölüm sırasını, içerik kurallarını ve placeholder'ları** al; HTML/CSS görünümünü design-system-v9.md belirler.
> - **Conic glow KULLANMA** (blog skill'inde var, kategoride yok).
> - **Floating ToC / İçindekiler EKLEME.**
> - `design-system-v9.md`'deki paylaşılan `<style>` bloğunu body'nin **en başına bir kez** ekle (gp-layer + FAQ nabzı için gerekli).
> - Site koyu temalı; açık zeminli bloklar göze batar, kullanma.

## 1. H2 Main Heading + Intro Paragraph

```html
<h2>[Primary Keyword] [Secondary if relevant]: GeForce NOW ile Bulutta Oyna ([YEAR])</h2>

<p>[Definition: "[Kategori adı], ... bir oyun türüdür." or similar.] [Sub-types named.] <a href="https://gameplus.com.tr/gfn">[anchor]</a> kütüphanesinde [VERIFIED COUNT] [tür] oyunu yer alıyor ve bu yapımların tamamı NVIDIA'nın RTX destekli bulut sunucuları üzerinden, güçlü bir bilgisayara ihtiyaç duymadan oynanabiliyor.</p>
```

## 2. TLDR Block (Yeşil Sol Kenarlı)

```html
<div class="tldr-block" style="background-color:#161616;padding:18px 20px;border-left:5px solid #FFC900;margin:24px 0;border-radius:4px;">
  <h2 style="margin:0 0 10px 0;font-size:1.15em;color:#333;">Hızlı Özet</h2>
  <ul style="margin:0;padding-left:20px;color:#444;">
    <li><strong>Kütüphane:</strong> [N+] [kategori] oyunu (yuvarlanmış, exact değil); [kısa tür açıklaması].</li>
    <li><strong>Öne Çıkan Yapımlar:</strong> <em>[Game1]</em>, <em>[Game2]</em>, <em>[Game3]</em>, <em>[Game4]</em>.</li>
    <li><strong>Alt Türler:</strong> [Sub1], [Sub2], [Sub3], [Sub4].</li>
    <li><strong>[4. Spesifik Özellik]:</strong> [Çok oyunculu, ücretsiz erişim, RTX desteği, kooperatif, vb. — kategoriye özel].</li>
  </ul>
</div>
```

**Madde sayısı 3-6 (duruma göre); her zaman 4 şart değil.** Son madde olarak yaş/PEGI yazma; ilgili kategori için en güçlü ek özelliği seç.

## 3. Türkiye Sunucu Paragrafı

```html
<p>Türkiye'deki GAME+ sunucuları sayesinde [Spesifik Oyun 1] gibi [özellik 1], [Spesifik Oyun 2] gibi [özellik 2] ve [Spesifik Oyun 3] gibi [özellik 3] elde edebilirsin. [İndirme yok / cihaz bağımsız gibi ek faydalar].</p>
```

## 4. Info-Card (4 Badge Grid)

```html
<div class="info-card" role="complementary" style="background-color:#fff;border:1px solid #e5e7eb;border-radius:8px;padding:16px;margin:24px 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:16px;">
  <div>
    <span style="display:block;font-size:0.78em;color:#6b7280;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px;">Kütüphane Boyutu</span>
    <span style="font-size:1.1em;font-weight:600;color:#111827;">[N+] Oyun (yuvarlanmış, exact değil)</span>
  </div>
  <div>
    <span style="display:block;font-size:0.78em;color:#6b7280;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px;">Öne Çıkan Yapım</span>
    <span style="font-size:1.1em;font-weight:600;color:#111827;">[Featured Game]</span>
  </div>
  <div>
    <span style="display:block;font-size:0.78em;color:#6b7280;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px;">[Badge 3 Label]</span>
    <span style="font-size:1.1em;font-weight:600;color:#111827;">[Badge 3 Value]</span>
  </div>
  <div>
    <span style="display:block;font-size:0.78em;color:#6b7280;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:4px;">[Badge 4 Label]</span>
    <span style="font-size:1.1em;font-weight:600;color:#111827;">[Badge 4 Value]</span>
  </div>
</div>
```

**Badge 3 ve 4 önerileri (kategoriye göre seç):**
- Alt Tür Sayısı
- Çok Oyunculu Destek
- Ücretsiz Yapımlar
- RTX Desteği
- Kooperatif Modu
- Düşük Gecikme (40 ms)
- Mağaza (Steam/Epic/Xbox/Ubisoft Connect)
- Maks. Oturum (8 Saat)

**Asla kullanma:** Türkiye Sunucusu (sabit), Yaş Aralığı / PEGI, Önerilen Paket, Mod Desteği.

## 5. H3 Popüler Oyunlar + Tablo

```html
<h3>GeForce NOW Türkiye'deki En Popüler [Tür] Oyunları</h3>

<p>[Tabloya giriş cümlesi. Lisans hatırlatması doğal olarak gömülü.]</p>

<div class="table-wrap" style="overflow-x:auto;margin:16px 0 24px;">
  <table style="width:100%;border-collapse:collapse;font-size:0.95em;background:#fff;border:1px solid #e5e7eb;">
    <thead>
      <tr style="background:#f3f4f6;">
        <th style="padding:12px;text-align:left;border-bottom:2px solid #e5e7eb;font-weight:600;">Oyun</th>
        <th style="padding:12px;text-align:left;border-bottom:2px solid #e5e7eb;font-weight:600;">Alt Tür</th>
        <th style="padding:12px;text-align:left;border-bottom:2px solid #e5e7eb;font-weight:600;">Platform</th>
        <th style="padding:12px;text-align:left;border-bottom:2px solid #e5e7eb;font-weight:600;">Öne Çıkan Özellik</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid #e5e7eb;">
        <td style="padding:12px;vertical-align:top;"><strong>[Game Name]</strong></td>
        <td style="padding:12px;vertical-align:top;">[Sub-genre]</td>
        <td style="padding:12px;vertical-align:top;">[Steam, Epic, Xbox vb.]</td>
        <td style="padding:12px;vertical-align:top;">[1 cümlelik öne çıkan özellik]</td>
      </tr>
      <!-- 8-12 row total. Game adı her zaman <strong>. Yaş kolonu YOK. -->
    </tbody>
  </table>
</div>

<p>[Tablo sonrası geçiş + içerik link örneği (örn. /gfn/oyunlar/ilgili-kategori).]</p>
```

**Yaş kolonu kullanma.** "Erişim" (Ücretsiz / Lisanslı) kolonu uygun kategoriler için iyi alternatif.

## 6. Editor Note #1 (Mavi Sol Kenarlı)

```html
<div class="editor-note" style="background-color:#eef6ff;border-left:4px solid #2563eb;padding:14px 16px;margin:24px 0;border-radius:4px;">
  <div style="font-weight:600;margin-bottom:6px;color:#1e40af;">📝 Game+ Editör Notu</div>
  <p style="margin:0;">[Faktüel ek bilgi: GOTY ödülü, geliştirici stüdyo durumu, beklenmedik mekanik, vb. Yaş/PEGI/yıl iddiası YOK.]</p>
</div>
```

## 7. Avantajlar Listesi

```html
<h3>[Tür] Oyunlarını Bulutta Oynamanın Avantajları</h3>

<p>[Türün donanım açısından özel zorluklarını tanımlayan kısa bir giriş.]</p>

<ul>
  <li><strong>[Bold lead-in].</strong> [Spesifik oyun adı verilen, 2-3 cümlelik açıklama.]</li>
  <!-- 5-7 madde. Her madde bold lead-in + somut oyun ismi içerir. -->
</ul>
```

## 8. Dynamic CTA (Dark Mode)

Tip seç: **C3** (badge+headline) / **C4** (stat banner) / **D2** (dual button). Template'ler `cta-templates.md` içinde.

## 9. License Callout (Sarı, Zorunlu Bir Kere)

```html
<div class="callout" style="background-color:#fef3c7;border-left:4px solid #f59e0b;padding:12px 16px;margin:24px 0;border-radius:4px;">
  <div style="font-weight:600;margin-bottom:6px;">ℹ Hatırlatma</div>
  GeForce NOW oyun satmaz; mevcut Steam, Epic Games Store, Xbox, EA App veya Ubisoft Connect kütüphanendeki lisansları bulut üzerinden çalıştırır. [Kategori adı] oynamak için ilgili platformda oyuna sahip olman gerekir.
</div>
```

## 10. Nasıl Oynanır (4 Adım)

```html
<h3>GeForce NOW'da [Tür] Oyunları Nasıl Oynanır?</h3>

<p>[Tek cümle giriş.]</p>

<ol>
  <li><strong>Uygulamayı indir.</strong> [PC, Mac, iOS, Android, akıllı TV açıklaması.]</li>
  <li><strong>Oyun platformunu bağla.</strong> [Steam/Epic/Xbox/EA App/Ubisoft Connect hesabı bağlama.]</li>
  <li><strong><a href="https://gameplus.com.tr/gfn/oyunlar">GeForce NOW oyunlar</a> listesinden oyununu seç.</strong> [Kütüphane adetinden bahseden açıklama.]</li>
  <li><strong>Oynamaya başla.</strong> [Bulut sunucu + cihaza aktarım + senkronizasyon.]</li>
</ol>

<p>[Bulut kayıt senkronizasyonu + lisans hatırlatması.]</p>
```

## 11. Sub-Genre Rehberi (4-7 H4)

```html
<h3>Hangi [Tür] Sana Uygun?</h3>

<p>[Alt tür çeşitliliği giriş cümlesi.]</p>

<h4>[Alt Tür 1]</h4>
<p>[Mekanik tanımı 2 cümle.]</p>
<p>[GFN'deki temsilcileri 3-4 cümle. Spesifik oyun isimleri.]</p>
<p><strong>Öne çıkan [alt tür] oyunları:</strong></p>
<ul>
  <li>[Oyun 1] (kısa özellik)</li>
  <!-- 3-5 örnek -->
</ul>

<!-- Diğer alt türler için aynı pattern. Toplamda 4-7 H4. -->
```

## 12. Editor Note #2 (Sub-Genre Section İçinde)

Yapı Editor Note #1 ile aynı. Tipik konum: ilk alt tür H4'ünden hemen ÖNCE (giriş cümlesinin altında). İçerik kategoriye özel faktüel bilgi.

## 13. Teknik Ayarlar Tablosu

```html
<h3>Teknik Ayarlar ve Sistem Önerileri</h3>

<p>[Tek cümle giriş.]</p>

<div class="table-wrap" style="overflow-x:auto;margin:16px 0 24px;">
  <table style="width:100%;border-collapse:collapse;font-size:0.95em;background:#fff;border:1px solid #e5e7eb;">
    <thead>
      <tr style="background:#f3f4f6;">
        <th style="padding:12px;text-align:left;border-bottom:2px solid #e5e7eb;font-weight:600;width:30%;">Konu</th>
        <th style="padding:12px;text-align:left;border-bottom:2px solid #e5e7eb;font-weight:600;">Öneri</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:12px;vertical-align:top;"><strong>İnternet hızı</strong></td><td style="padding:12px;vertical-align:top;">720p/60 FPS için en az 15 Mbps, 1080p/60 FPS için en az 25 Mbps. Gecikme 80 ms'nin altında olmalı.</td></tr>
      <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:12px;vertical-align:top;"><strong>Bağlantı türü</strong></td><td style="padding:12px;vertical-align:top;">Kablolu Ethernet en kararlı. 5 GHz Wi-Fi de iş görür.</td></tr>
      <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:12px;vertical-align:top;"><strong>Kontrol seçenekleri</strong></td><td style="padding:12px;vertical-align:top;">[Kategoriye özel: gamepad / fare+klavye / dokunmatik.]</td></tr>
      <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:12px;vertical-align:top;"><strong>[Kategoriye özel satır]</strong></td><td style="padding:12px;vertical-align:top;">[Spesifik öneri.]</td></tr>
      <tr><td style="padding:12px;vertical-align:top;"><strong>Kayıt dosyaları</strong></td><td style="padding:12px;vertical-align:top;">Bulut kayıt senkronizasyonu aktif.</td></tr>
    </tbody>
  </table>
</div>
```

**Mod desteği satırı YOK.** Spesifik TV yıl bilgisi YOK. Yaş bilgisi YOK.

## 14. Performance vs Ultimate Karşılaştırması (Nötr)

```html
<h3>Performance ve Ultimate Karşılaştırması</h3>

<p>İki paket arasındaki farklar donanım sınıfı, çözünürlük tavanı, FPS sınırı ve oturum süresinden ibaret:</p>

<div class="table-wrap" style="overflow-x:auto;margin:16px 0 24px;">
  <table style="width:100%;border-collapse:collapse;font-size:0.95em;background:#fff;border:1px solid #e5e7eb;">
    <thead>
      <tr style="background:#f3f4f6;">
        <th style="padding:12px;text-align:left;border-bottom:2px solid #e5e7eb;font-weight:600;">Özellik</th>
        <th style="padding:12px;text-align:left;border-bottom:2px solid #e5e7eb;font-weight:600;">Performance</th>
        <th style="padding:12px;text-align:left;border-bottom:2px solid #e5e7eb;font-weight:600;">Ultimate</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:12px;vertical-align:top;"><strong>Oyun sistemi</strong></td><td style="padding:12px;vertical-align:top;">GeForce RTX / 8 vCPU</td><td style="padding:12px;vertical-align:top;">GeForce RTX 4080 / 16 vCPU</td></tr>
      <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:12px;vertical-align:top;"><strong>Maksimum çözünürlük</strong></td><td style="padding:12px;vertical-align:top;">1440p QHD</td><td style="padding:12px;vertical-align:top;">5K'ye kadar (4K HDR dahil)</td></tr>
      <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:12px;vertical-align:top;"><strong>Maksimum FPS</strong></td><td style="padding:12px;vertical-align:top;">60 FPS</td><td style="padding:12px;vertical-align:top;">240 FPS'e kadar</td></tr>
      <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:12px;vertical-align:top;"><strong>Oturum süresi</strong></td><td style="padding:12px;vertical-align:top;">6 saat</td><td style="padding:12px;vertical-align:top;">8 saat</td></tr>
      <tr><td style="padding:12px;vertical-align:top;"><strong>DLSS 3 ve Reflex</strong></td><td style="padding:12px;vertical-align:top;">Kapalı</td><td style="padding:12px;vertical-align:top;">Açık</td></tr>
    </tbody>
  </table>
</div>

<p>[Nötr karşılaştırma: "İki paket de [kategori] oyunlarını çalıştırır." + factual farklar. "Performance yeterli" / "Ultimate öneririz" YASAK.]</p>
```

## 15. FAQ Accordion ("X Hakkında Sık Sorulan Sorular")

```html
<h3>[Kategori Adı] Hakkında Sık Sorulan Sorular</h3>

<div class="faq-block">

  <details class="faq-item" style="margin-bottom:10px;border:1px solid #e5e7eb;border-radius:6px;overflow:hidden;">
    <summary class="faq-q" style="padding:14px 16px;cursor:pointer;background:#f9fafb;font-weight:600;">[Soru metni — direkt summary içinde, h4 wrap YOK]</summary>
    <div class="faq-a" style="padding:12px 16px;border-top:1px solid #e5e7eb;background:#fff;">
      <p style="margin:0;">[Cevap. 40-60 kelime.]</p>
    </div>
  </details>
  
  <!-- 4-6 soru toplam. Body'de cevaplanmış soruları FAQ'a koyma. -->

</div>
```

**Soru metni doğrudan `<summary>` içinde** — `<h4>` ile sarılmaz (renderer'larda "Details" placeholder sorununa yol açıyordu).

## 16. Fix CTA (Sabit — Tüm İçeriklerde Aynı)

Template `cta-templates.md` içinde. Kısaca:
- Dark mode card (#0f172a bg)
- "GeForce NOW" (NOW yeşil) + [PERFORMANCE] [ULTIMATE] kapsül etiketler
- Headline: "Tek üyelik, hazır kütüphane."
- Açıklama
- Buton: "GeForce NOW Paketlerini İncele →"

## 17. Final CTA Paragrafı

```html
<h3>[Tür] Dünyasına Hemen Adım At</h3>

<p>[2-3 cümlelik CTA paragrafı. Tabloda geçen 2-3 spesifik oyun adıyla başlar. "Güçlü bir bilgisayara ihtiyacın yok." cümlesi. Üç imperatif kapanış: kütüphaneni bağla, paket seç, oynamaya başla.]</p>
```

## Hedef Toplam

- **Kelime sayısı (HTML tag'ler hariç):** 1800-2400
- **H3 sayısı:** 8-10
- **H4 sayısı:** 4-7 (sub-genre)
- **Tablo sayısı:** 3 (popüler, teknik, paket)
- **Editor note sayısı:** 2
- **CTA sayısı:** 2 (Dinamik + Fix)
- **Callout sayısı:** 1 (lisans)
- **FAQ accordion:** 4-6 item

## Internal Link Limitleri

- `/gfn` → intro (1 kere) + ayrıca bir Dynamic CTA hedefi olabilir
- `/gfn/oyunlar` → 1 kere (Nasıl Oynanır step 3)
- `/gfn/paketler` → SADECE **Fix CTA** (1 kere). Body inline'da YOK, Dynamic CTA'da YOK.
- **Dynamic (sayfa-ortası) CTA** → `/gfn` | `/geforce-now-nedir` | `/firsatlar` (paketler DEĞİL, kategori self-link DEĞİL)
- 3-4 ilgili kategori URL'i → her biri 1 kere
- Toplam unique internal link: 6-8

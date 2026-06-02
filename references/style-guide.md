# Style Guide

Hard rules and tone preferences extracted from multiple rounds of Gameplus team revisions. Apply from the first draft.

## Voice

- **Second person, informal "sen"**, never "siz". Reader is a fellow gamer.
- **Authoritative but not lecturing.** No "Bilmiyor olabilirsin ama..." or "Sana açıklayayım..."
- **Not blog-style.** Categories are utility pages. No "Hazır mısın?" rhetorical openers.
- **Confident on technical claims.** "GeForce NOW'un RTX destekli sunucuları, Cyberpunk 2077'yi ray tracing açıkken 60 FPS'te çalıştırır." Not: "Çalıştırabilir."

## Banned words and phrases

### "başlık" — replace with "oyun" or "yapım"

**Wrong:** "RTS başlıklarında girdi gecikmesi", "rekabetçi başlıklar", "en ağır başlıklar"
**Right:** "RTS oyunlarında girdi gecikmesi", "rekabetçi oyunlar", "en ağır oyunlar"

Banned across all forms: başlıklarda, başlıklara, başlığını, başlığa, vb.

### em dash (—) — never

Use semicolons, commas, or restructure. Hyphens (-) in compound words ("hack-and-slash") are fine.

### Generic anchors

**Wrong:** "buraya tıkla", "bu sayfa", "linke tıklayarak"
**Right:** Keyword-rich anchors from `url-anchor-mapping.md`.

### "kategori" in section headings

**Wrong:** "Aksiyon Severlerin Keşfedebileceği Diğer Kategoriler"
**Right:** Distribute links across body in natural sentences. No dedicated section.

### Marketing clichés

- "Hazır mısın?" (only end-CTA acceptable, not intros)
- "Soluksuz aksiyon"
- "Vazgeçilmez deneyim"
- "Mutlaka oynanmalı"
- "Kaçırılmayacak"
- "Efsane oyunlar" (once max)
- "Buluta taşı" (yapay metafor)

## Banned content (yeni eklenenler)

### Steam Workshop iddiası — yasak

Mod desteği yapım bazında değişir ve doğrulanmadı. Şunlar yazılmaz:
- "Steam Workshop üzerinden mod yükleme destekleniyor"
- "Kapsamlı mod desteği"
- "Crusader Kings III gibi yapımlarda topluluk modları aktif"

Eğer mod konusu zorunlu geçecekse: "DLC desteği" veya "uzun ömürlü canlı servis modeli" kullan.

### PEGI / Yaş referansları — yasak

- "PEGI 3+", "PEGI 7", "PEGI 12+" gibi etiketler YOK
- "10+ yaş için", "çocuğa uygun yaş", "yaş aralığı" YOK
- Aile dostu kategorisinde bile oyunları yaş ile değil; co-op modu, sanat tarzı, tema ile tanımla

### Spesifik TV model yılları — yasak

**Wrong:** "2021/2022 LG ve Samsung akıllı TV'lerinde GeForce NOW uygulaması mevcut"
**Right:** "LG ve Samsung akıllı TV'lerinde GeForce NOW uygulaması mevcut"

### Paket önerisi — yasak

**Wrong:** "Performance paketi çoğu strateji oyuncusu için yeterlidir", "Ultimate paketi tercih edebilirsin"
**Right:** Performance ve Ultimate karşılaştırması özellikleri nötr listeler. "İki paket de [kategori] oyunlarını çalıştırır." gibi nötr ifadeler.

H3 başlığı da prescriptive olmaz:
- **Wrong:** "Hangi Paket Strateji İçin Uygun?"
- **Right:** "Performance ve Ultimate Karşılaştırması"

## Required emphases

### License disclaimer

Sarı callout component'i ile bir kere zorunlu. Body'de natural mention de OK ama component zorunlu.

### Türkiye sunucusu vurgusu

En az bir kere body'de geçer (intro veya avantajlar). Info-card badge olarak KULLANILMAZ ("Türkiye Sunucusu: Aktif" — sabit bilgi, badge değeri katmaz).

### "Güçlü bir bilgisayara ihtiyacın yok"

CTA paragrafında bir kere. Intro'da da olabilir.

## Formatting

- **Game names** `<strong>` ile sarmalanır (tablolarda ve listelerde).
- **® ve ™** yayıncının kullanımına uygun (Diablo®, Diablo® II: Resurrected™).
- **Numbers**: 60 FPS, 25 Mbps, 4K, 1440p (boşluk ile).
- **Time format**: 40 ms, 60 Hz, 6 saat.
- **Avoid all-caps** — `<strong>` kullan.

## Paragraph rhythm

- Average paragraph: 2-4 sentences.
- No walls of text.
- Mix sentence lengths.
- Sub-genre H4 paragraphs slightly longer (4-5 sentences).

## Internal link density

- **Total unique links:** 6-8 across the whole piece.
- **Required:** `/gfn` (1x), `/gfn/oyunlar` (1x).
- Plus 3-4 related category URLs from `category-pages.md`.
- **`/gfn/paketler` SADECE CTA component'lerinde** (2x: Dynamic + Fix). Body inline'da YOK.
- **No URL linked twice in body.** CTA component'leri istisna (visual unit).

## NO YouTube embeds

Blog posts include YouTube under each game. Categories do not. Strip any `<em>YouTube video:</em>` placeholders.

## Tense and time references

- Present tense for game descriptions.
- Simple past or perfect for library updates.
- Avoid month references that go stale ("bu ay", "son haftalarda"). Evergreen.
- Year in H2 (2026) is OK — update annually.

## CTA copy

- Kısa, somut, oyun ismi geçen cümleler.
- "Anında erişim sağlar", "buluta taşır" gibi yapay çeviri ifadelerden kaçın.
- Spesifik stat veya gerçek bilgi ekle (40 ms, 600+ oyun, ücretsiz).
- Fix CTA buton metni: "GeForce NOW Paketlerini İncele →"
- Dynamic CTA buton metni: "GeForce NOW Paketleri →"

## Examples to study

`examples/` folder eski pattern içerir. Yeni pattern için Dispatch projesindeki `*-icerik-deneme-2.html` dosyalarına bak. Aile-dostu ve strateji en güçlü modern örnekler.

# Post-Content QA Checklist

Run before delivering. Items grouped by *why these checks exist* — çoğu past revision'larda fail eden noktalardan geliyor.

## A. Yapısal Bileşenler (Yeni Model)

- [ ] **TLDR block** intro'dan sonra var (yeşil sol kenar `#76b900`, **3-6 list item** duruma göre, son madde yaş/PEGI değil)
- [ ] **Info-card** Türkiye sunucu paragrafından sonra var (4 badge: Kütüphane Boyutu + Öne Çıkan + 2 kategori-spesifik)
- [ ] **Tablolar** `<div class="table-wrap">` ile sarılı ve inline style'lı (border, padding, vertical-align)
- [ ] **Editor Note #1** popüler oyunlar tablosundan sonra (mavi sol kenar `#2563eb`)
- [ ] **Dynamic CTA** avantajlar listesinden sonra (dark mode #0f172a)
- [ ] **License callout** avantajlar+CTA sonrası (sarı sol kenar `#f59e0b`)
- [ ] **Editor Note #2** sub-genre rehberi içinde / öncesinde
- [ ] **FAQ accordion** (4-6 `<details>` item, summary direkt metin, h4 nested YOK)
- [ ] **Fix CTA** final paragraf öncesinde (dark mode + GeForce NOW + Performance/Ultimate badges)

## B. İçerik Kuralları (Yasaklar)

- [ ] **0 em dash (—)**: `grep -c '—' <file>` → 0
- [ ] **0 "başlık" body'de**: `grep -c '\bbaşlık' <file>` → 0 (heading dışında)
- [ ] **0 "Steam Workshop" / "mod desteği" claim**: `grep -c 'Steam Workshop' <file>` → 0
- [ ] **0 PEGI referansı**: `grep -c 'PEGI' <file>` → 0
- [ ] **0 explicit yaş etiketi** ("10+", "PEGI 7", "7-12 yaş grubu", vb.)
- [ ] **0 spesifik TV model yılı** ("2021/2022", "2024 modeli LG", vb.)
- [ ] **0 paket önerisi cümlesi** ("Performance yeterli", "Ultimate öneririz")
- [ ] **0 "GAME+ paketi" anchor** (eski anchor → "GeForce NOW fiyat")

## C. Game Sayısı Doğrulama

- [ ] **Game count Playwright ile doğrulandı** (URL'i ziyaret et, OYNAT butonlarını say)
- [ ] **TLDR'daki sayı** Playwright sonucuyla aynı
- [ ] **Info-card "Kütüphane Boyutu" badge'i** Playwright sonucuyla aynı
- [ ] **Intro paragrafı**ndaki sayı doğru
- [ ] **FAQ cevabı**ndaki sayı doğru

## D. Link Yapısı

- [ ] **`/gfn` linki** intro'da bir kere (anchor: "GeForce NOW" veya benzeri)
- [ ] **`/gfn/oyunlar` linki** Nasıl Oynanır step 3'te bir kere (anchor: "GeForce NOW oyunlar")
- [ ] **`/gfn/paketler` linki** SADECE CTA component'lerinde (Dynamic + Fix, 2 kere). Body inline'da YOK.
- [ ] **3-4 ilgili kategori URL'i** body içinde dağıtılmış (alt türler, related categories)
- [ ] **No URL linked twice in body** (CTA card'lar visual unit, ayrı kategori)
- [ ] **Anchor textler** `url-anchor-mapping.md` ile uyumlu
- [ ] **No external links** (sadece gameplus.com.tr)

## E. Heading Hiyerarşisi

- [ ] **H2** main heading: primary keyword + "GeForce NOW" + "Bulutta Oyna" + year
- [ ] **H3 sayısı**: 8-10
- [ ] **H4 sayısı**: 4-7 (sub-genre alt türler)
- [ ] **FAQ heading**: "[Kategori Adı] Hakkında Sık Sorulan Sorular"
- [ ] **Paket heading**: "Performance ve Ultimate Karşılaştırması" (prescriptive değil)
- [ ] **H4 nested in `<summary>` YOK**: FAQ soru metni direkt summary içinde

## F. İçerik Derinliği

- [ ] **Kelime sayısı**: 1800-2400 (sed ile tag strip + wc -w)
- [ ] **Popüler oyunlar tablosu**: 8-12 satır
- [ ] **Avantajlar listesi**: 5-7 madde, her birinde bold lead-in + spesifik oyun
- [ ] **Nasıl oynanır**: 4 adım (3 değil, 6 değil)
- [ ] **Sub-genre H4**: 4-7 tane, her biri 100-150 kelime
- [ ] **Teknik ayarlar tablosu**: 5 satır (mod desteği satırı YOK)
- [ ] **Paket karşılaştırma tablosu**: 5 satır (Oyun sistemi, Çözünürlük, FPS, Oturum, DLSS 3)
- [ ] **FAQ**: 4-6 soru (body'de zaten cevaplanmış soruları FAQ'a koyma)
- [ ] **CTA paragrafı**: 2-3 spesifik oyun ismi var

## G. Zorunlu Vurgular

- [ ] **Lisans hatırlatması** sarı callout component'inde var
- [ ] **Türkiye sunucusu / düşük gecikme** body'de en az 1 kere
- [ ] **"Güçlü bir bilgisayara ihtiyacın yok"** CTA paragrafında var

## H. AI Citation Hazırlığı (GEO)

- [ ] **İlk cümle clean definition**: "[Kategori] oyunları, ... bir oyun türüdür."
- [ ] **Game names `<strong>`** tablolarda ve listelerde tutarlı
- [ ] **Tables `<thead>`, `<tbody>`, semantic `<th>`** ile yapılı
- [ ] **Her H3 section standalone answer block** olabilmeli (içerikte "Yukarıda gördüğümüz gibi..." yok)

## I. Hızlı Bash Audit (Tek Seferde)

```bash
F=<file>.html
echo "Em dash: $(grep -c '—' $F)" 
echo "başlık: $(grep -c '\bbaşlık' $F)"
echo "Steam Workshop: $(grep -c 'Steam Workshop' $F)"
echo "PEGI: $(grep -c '\bPEGI' $F)"
echo "Words: $(sed 's/<[^>]*>//g' $F | wc -w)"
echo "H3: $(grep -c '<h3>' $F)"
echo "H4: $(grep -c '<h4' $F)"
echo "details: $(grep -c '<details' $F)"
echo "Duplicate URLs:" && grep -oE 'href="[^"]+"' $F | sort | uniq -d
echo "All links:" && grep -oE 'href="[^"]+"' $F | sort -u
```

Hepsi 0 / temiz değilse fix gerekli.

## J. 30 Saniye Read Test

1. İlk 5 saniyede: kategori ve değer önerisi anlaşılıyor mu?
2. 15. saniyede: spesifik bir oyun ismi gözüne çarpıyor mu?
3. 30. saniyede: paket seçimi ve nasıl başlayacağı net mi?

Herhangi biri "hayır" ise yapı kullanıcıyı yetersiz hizmet ediyor.

## K. Eski Revision Themes (Önceden Yakalananlar)

1. **"Çok jenerik geldi."** Fix: spesifik oyun isimleri çoğalt, abstract claim'leri concrete örnekle değiştir.
2. **"Türkçe karakterler doğru kullanılmamış."** Fix: ı, ş, ç, ğ, ö, ü kontrol et.
3. **"Linkler yığılmış."** Fix: 3+ link'li `<ul>`'leri böl, body'ye yay.
4. **"Aynı kelime tekrarı."** Fix: anchor text varyasyonu, "oyun"/"yapım" alternasyonu.
5. **"Daha kısa yerine daha derin olsun."** Fix: sub-genre H4'leri zenginleştir, intro padding ekleme.
6. **"PEGI/yaş referansı koyma."** (yeni) Fix: yaş bilgisi içeren badge/kolon/cümle yok.
7. **"Spesifik TV yıl bilgisi verme."** (yeni) Fix: "LG ve Samsung" formuna döndür.
8. **"Paket önerme."** (yeni) Fix: karşılaştırma nötr, recommendation cümleleri çıkar.
9. **"FAQ accordion'da 'Details' görünüyor."** (yeni) Fix: `<summary>` içine direkt soru metni, h4 nested yapma.

## v10.2 görsel kontrolleri (Game+ UI)
- [ ] **0 yeşil kalıntı** — `#76b900` / `rgba(118,185,0,*)` yok; tek vurgu `#FFC900`.
- [ ] **0 `gp-conic` ve 0 `floating-toc`** — kategori kuralı.
- [ ] **Callout barı `border-left` DEĞİL** — flex + ayrı 4px yuvarlak uçlu bar div'i (blog `render_editor_note`/`render_highlight` ile birebir).
- [ ] **TLDR maddeleri sarı `•`** (✓ tik yok); gövde `<ul>` nokta rengi de `#FFC900` (`ul li::marker`).
- [ ] **Stat kartlarında DEĞER üstte**, sarı New Science, kart içinde ortalı.
- [ ] **Tablo sütun başlıkları sarı ve ORTALI** (mobilde de).
- [ ] **CTA GA4 id'leri var:** `category-dynamic-cta` + `category-packages-button`.
- [ ] Çıktıda `{{` / `}}` yok (f-string kaçış hatası CSS'i geçersiz kılar).

---
name: gameplus-category-content
description: Generate SEO and GEO optimized category page content for gameplus.com.tr (GeForce NOW Turkey, powered by GAME+). Produces ~2000-word Turkish HTML category content with inline Gemini-pattern styling, TLDR block, info-card badges, dark-mode dynamic and fixed CTAs, FAQ accordion, editor notes, and DataForSEO-driven keyword research. Use whenever the user requests content for a Gameplus GFN category page (any URL like gameplus.com.tr/gfn/oyunlar/*), or says things like "gameplus kategori içeriği yaz", "gfn kategori sayfası", "gameplus category content", "gameplus için içerik", "geforce now kategori yazısı", "gfn oyunlar sayfası içeriği". Trigger even when the user only pastes a Gameplus category URL with an implicit content request, or mentions revising a category page they already have. Do NOT use this for Gameplus blog posts (those have a different tone, structure, and HTML enrichment pattern).
---

# Gameplus Category Content Generator

This skill produces SEO and GEO optimized HTML category page content for **gameplus.com.tr** (NVIDIA GeForce NOW powered by GAME+ Türkiye). Category pages live under `/gfn/oyunlar/*` and accompany the game grid with a long-form article below it.

The skill bakes in the visual + structural pattern established with the Gameplus team through multiple revision rounds. **Görsel dil v10.2 "Game+ UI"dır** (`references/design-system-v10.md`): tek vurgu sarı `#FFC900` (yeşil #76b900 KALKTI), `#161616` kartlar, `#0D0D0D` stat kartları, New Science SemiBold Extended başlıklar, sarı `•` TLDR, `#1E1E18` tablo başlığı. Blog skill'iyle (`gameplus-blog-enrich-v2`) aynı görsel dil; tek fark kategoride **conic glow ve floating ToC kullanılmaz**. It also bakes in content rules: no Steam Workshop claims, no PEGI/age recommendations, no specific TV model years, no prescriptive package recommendations.

## When to invoke

Trigger immediately when the user:
- Pastes any URL under `gameplus.com.tr/gfn/oyunlar/*` and asks for content
- Says "kategori içeriği", "kategori sayfası", "category content" in a Gameplus context
- Asks to write or revise content for a GFN game type (e.g., "MMO için içerik yaz", "yarış oyunları sayfasına metin lazım")
- Says "gameplus için içerik", "gfn için içerik", "gameplus geforce now içerik"

Do not trigger for blog posts. Blog content uses a different methodology with image enrichment, YouTube embeds, and a longer narrative format.

## High-level workflow

Always go through these 6 phases.

### Phase 1: Research the target category

1. Identify the target URL and primary keyword(s) from `references/category-pages.md`.
2. **Verify the live game count via Playwright** — navigate to the URL, scroll to bottom, count "OYNAT" buttons. This is the value behind "Kütüphane Boyutu" and the count referenced in TLDR/body/FAQ/CTA stat. **Sayıyı her zaman AŞAĞI yuvarlanmış "X+" biçiminde yaz, asla exact tam sayı kullanma** (434 → 400+, 69 → 60+, 14 → 10+; ≥100 için en yakın 100 aşağı, <100 için en yakın 10 aşağı). Exact sayı hem yapay görünür hem de kütüphane büyüdükçe bayatlar. Aynı yuvarlanmış değeri badge, TLDR, gövde, FAQ ve C4 stat'ında tutarlı kullan.
3. Note the top 12-15 games currently in the grid — these inform the popular games table later.

### Phase 2: DataForSEO keyword and SERP research

Follow `references/dataforseo-workflow.md`. The 8-step flow in short:

1. `kw_data_google_ads_search_volume` for 10-15 candidate keywords (volume + competition).
2. `dataforseo_labs_bulk_keyword_difficulty` for the same set (KD scores).
3. `dataforseo_labs_search_intent` to confirm intent classification.
4. `dataforseo_labs_google_keyword_suggestions` for long-tail expansion.
5. After steps 1-4, **lock in 2-4 target keywords** that fit the category.
6. `serp_organic_live_advanced` on those keywords (top 20, PAA, AI Overviews).
7. **Competitor keyword mining:** For each target keyword, take top 5 ranking URLs; for each URL, `dataforseo_labs_google_ranked_keywords`; aggregate keywords appearing on 2+ competitors with vol ≥ 100 and contestable KD.
8. `ai_optimization_chat_gpt_scraper` on the most relevant query to see which entities ChatGPT cites.

Location is always `2792` (Türkiye), language `tr`. The DataForSEO MCP namespace is `mcp__dfs-mcp__*` or `mcp__dataforseo__*`.

### Phase 3: Plan the content

Use `references/structure-template.md` for the section skeleton. Confirm:

- **H2 main heading**: includes primary keyword + "GeForce NOW" + "Bulutta Oyna" + current year. Lead with the keyword.
- **Verified game count** from Phase 1 — used in TLDR, info-card badge, intro paragraph, and FAQ answer.
- **Popular games table**: 8-12 games drawn from the live grid, prioritizing ones AI Overview / ChatGPT cite.
- **Internal link plan**: list URLs you'll link to. Always include `/gfn`, `/gfn/oyunlar`. Add 3-4 contextually relevant category URLs from `references/category-pages.md`. Pick anchors from `references/url-anchor-mapping.md`. **CTA link kuralı (v11):** **Fix CTA** `/gfn/paketler`'e gider. **Dynamic (sayfa-ortası) CTA GFN paketlerine DEĞİL**, şu 3 sayfadan birine gider (kategoriler arasında rotasyon): `/gfn`, `/geforce-now-nedir`, **`/paketler` (GAME+ paketleri)**. **`/firsatlar` ARTIK KULLANILMAZ** (marka kararı). **Hiçbir CTA, içinde bulunduğu kategori sayfasına self-link VERMEZ.** Body içinde `/gfn/paketler` inline link kullanma.
- **Info-card 4 badges** — Kütüphane Boyutu (yuvarlanmış "X+", asla exact), Öne Çıkan Yapım, plus 2 category-specific (Alt Tür Sayısı, Çok Oyunculu, RTX Desteği, vb.). Never use Türkiye Sunucusu, PEGI/yaş, Mod Desteği, or prescriptive paket badges.
- **Dynamic CTA type** — pick C3 (badge + headline), C4 (stat banner), or D2 (dual button). See `references/cta-templates.md`.
- **2 editor notes** — one after popular games table, one in/before sub-genre rehberi section. Notes add factual depth (GOTY status, dev studio context, surprising mechanic), never age/PEGI/year claims.

### Phase 4: Write the content

Apply `references/style-guide.md` and `references/cta-templates.md` rigorously. Key rules:

- Turkish "sen" hitabı, informal but not chatty.
- ~2000 words target (1800-2400 acceptable).
- Avoid **başlık** in body text — use **oyun** or **yapım**.
- Never use the em dash (—). Use semicolons, commas, or restructure.
- **No YouTube links** in category content.
- **No Steam Workshop claims** — mod support varies per game.
- **No PEGI references, no age recommendations** (e.g., "10+", "PEGI 7"). Aile-dostu kategorisi bile yaş etiketi kullanmaz; oyunları co-op, sanat tarzı, tema üzerinden tanımlar.
- **No specific TV model years** ("2021/2022 LG ve Samsung" → "LG ve Samsung").
- **No prescriptive package recommendations** — Performance/Ultimate karşılaştırması özellikleri nötr şekilde gösterir, "Performance yeterli" / "Ultimate öneririz" gibi cümleler kullanmaz.
- License disclaimer must appear at least once via the yellow callout component.

### Phase 5: Apply structure components

> **GÖRSEL STİL — v11: blog skill'i ile TAM HİZALI.** Tipografi, renk, kart, tablo ve mühendislik
> kuralları blog skill'inden MİRAS ALINIR; kategoride ayrı bir tanım YOKTUR. Farklar ve gerekçeler:
> **`references/design-system.md`**.
>
> Uygulama: **`scripts/category_components.py`**. Elle HTML/CSS yazma, inline stil verme.
>
> ```python
> import sys; sys.path.insert(0, "<kategori-skill>/scripts")
> from category_components import *
>
> body  = "<h2>...</h2>" + render_tldr([...]) + render_info_card([...]) + ...
> body += render_category_dynamic_cta(baslik, aciklama, "https://gameplus.com.tr/paketler")
> body += render_category_fix_cta(baslik, aciklama)
> body += render_faq_accordion(faq) + render_faq_schema(faq)
> final = wrap_gp_content(CATEGORY_STYLE + "\n" + group_into_sections(body))   # Kural 22
> ```
>
> **Kategori kuralı:** conic glow YOK, floating ToC YOK, H1 YOK (gövde H2 ile başlar), YouTube YOK.
> `CATEGORY_STYLE` bu ailelerin CSS'ini zaten süzer.
>
> **Kural 22 - DOM genişliği.** `group_into_sections(body)` sarmalamadan hemen önce çağrılır ve
> `.gp-content` doğrudan çocuklarını `<section class="gp-sec">` altında gruplar. Gerekçe: Sitebulb
> "Avoid excessive DOM width" bir ebeveynde **60'tan fazla çocuk düğüm** olduğunda uyarıyor ve
> `.gp-content` sayfadaki en geniş ebeveyndi (kategori sayfalarında ortalama 141 çocuk düğüm).
> Bölme uyarlanabilir: önce `<h2>`, eşiği (varsayılan 50) aşan bölüm kalırsa `<h3>`, gerekirse `<h4>`.
> **Kategori gövdesinde tek H2 bulunduğu için bölme kendiliğinden H3'e iner.** `<style>` ve en üst
> seviye `<script>` (FAQ + kategori şeması) bölüm dışında kalır. Metne ve işaretlemeye dokunmaz;
> `verify_category_output` "DOM genişliği (Kural 22)" ile denetler. Ölçüm: 28 kategoride
> `.gp-content` ortalama 141 -> 35 çocuk düğüm, 1280 px ve 390 px'te 88 öğede yerleşim farkı sıfır.

**Kural 23 - Yazım ve CTA başlığı (v12.3).** "İndie" değil "Indie"; "Arcade"/"Indie" tür adı olarak
büyük harf (`yazim_normalize`, URL'lere dokunmaz). Fix CTA başlığı her zaman gerçek başlık
("Tek üyelik, hazır kütüphane."), rozet satırı (`PERFORMANCE ULTIMATE`) asla başlık olmaz.
Yazar başlığındaki dilbilgisi düzeltmeleri yalnız kullanıcı onayıyla `BASLIK_REVIZE`'ye girer.
Teslim öncesi `python3 scripts/denetim.py <çıktı-klasörü>` çalıştırılır (tablo, TLDR, CTA, SSS,
schema, yazım, Kural 21, DOM genişliği); SORUN 0 değilse teslim edilmez.

Section order (sabit):

1. **H2 main heading + intro paragraph** (with `/gfn` link)
2. **TLDR block** — yeşil sol kenarlı, **3-6 list item** (duruma göre; her zaman 4 şart değil)
3. **Türkiye sunucu paragrafı** — somut oyun örnekleri + gecikme stat'ı
4. **Info-card** — 4 badge grid
5. **H3 Popüler Oyunlar** + intro + styled table (table-wrap) + closing paragraph
6. **Editor Note #1** — mavi sol kenarlı, factual depth
7. **H3 Bulutta Oynamanın Avantajları** + intro + 5-7 bullet items
8. **Dynamic CTA** — dark mode (C3 / C4 / D2)
9. **License callout** — sarı, mandatory once
10. **H3 Nasıl Oynanır?** + 4-step ordered list
11. **H3 Hangi Tür Sana Uygun?** + 4-7 sub-genre H4 sections
12. **Editor Note #2** — placed in or before sub-genre section
13. **H3 Teknik Ayarlar** + styled table (5 rows, no mod desteği row)
14. **H3 Performance ve Ultimate Karşılaştırması** (neutral) + styled table + factual closing
15. **H3 Kapanış başlığı** + kapanış paragrafı
16. **Fix CTA** — `render_category_fix_cta`, id `category-packages-button` -> `/gfn/paketler`
17. **H3 [Kategori] Hakkında Sık Sorulan Sorular** + FAQ accordion (4-7 `<details>`, summary düz metin, iç içe H4 yok)
18. **FAQ Schema** — `render_faq_schema(pairs)`, görünen FAQ ile BİREBİR aynı içerik

> **v11 sıra değişikliği:** eskiden SSS -> Fix CTA -> kapanış paragrafı sırası vardı.
> Artık **kapanış -> CTA -> SSS**: sayfa SSS ile biter, kapanış paragrafı yukarı taşınır.

### Phase 6: QA against the checklist

**Önce otomatik kontrol, sonra elle checklist.**

```python
from category_components import verify_category_output, print_report, verify_source_preserved
ok = print_report(verify_category_output(final, oyun_sayisi_metni="200+ Oyun"))   # FAIL varsa TESLİM ETME
```

Otomatik doğrulananlar: tek stil bloğu, `.gp-content` sarmalayıcı, CSS scope, **H1 YOK + ilk başlık
H2**, floating ToC yok, YouTube yok, TLDR 3-6 madde, info-card, Editör Notu, lisans callout, madde
listesi, FAQ 4-7 + FAQPage JSON-LD, **sıra (kapanış -> CTA -> SSS)**, `/firsatlar` yok, dynamic CTA
hedefi izinli listede, Fix CTA tek, em dash yok, PEGI/yaş yok, Steam Workshop yok, çıktıda yorum yok,
gömülü font yok, inline onclick yok, yuvarlanmış oyun sayısı, etiket dengesi.

Ardından `references/checklist.md`'deki yargı gerektiren maddeler:
- 0 em dash
- 0 "başlık" in body text
- 0 "Steam Workshop" / "mod desteği" claims
- 0 "PEGI" references
- 0 explicit age recommendations
- 0 specific TV model years
- 0 paket recommendation sentences
- **0 exact kütüphane sayısı** — badge/TLDR/gövde/FAQ/C4 stat hepsi yuvarlanmış "X+" (örn. 400+, 60+); ham tam sayı (434, 69) YOK
- **0 CTA self-link** — hiçbir CTA içinde bulunduğu kategori sayfasına link vermiyor
- **Dynamic CTA GFN paketlerine gitmiyor** — Fix CTA `/gfn/paketler`; sayfa-ortası CTA `/gfn` | `/geforce-now-nedir` | `/paketler`. **`/firsatlar` hiçbir yerde yok.**
- **0 yapışık cümle** — cümle sonu noktadan sonra boşluk var (`kelime.Kelime` gibi birleşme YOK)
- Game count (rounded) matches Playwright verification
- All required components present (TLDR, info-card, 2 CTAs, license callout, FAQ accordion)
- 1800-2400 word range
- 8-12 popular games table rows
- 4-6 FAQ accordion items

## Output

Save the content in **two formats**:

1. **HTML** in the current working directory as `<category-slug>-icerik.html` (e.g., `mmo-icerik.html`). Article body HTML only — for CMS paste.

2. **DOCX** in the project archive at `/Users/Erdo/Desktop/Claude Projects/Game+ /İçerikler/` named after the URL with `/` replaced by `-`:
   - URL: `https://gameplus.com.tr/gfn/oyunlar/<slug>`
   - Filename: `gameplus.com.tr-gfn-oyunlar-<slug>.docx`

   **Not:** `html_to_docx.py` artık docx sonuna otomatik olarak "HTML Versiyon — CMS'e Gömmek İçin" bölümü ekler; render'lı içeriğin ardından stilli HTML kodu Courier ile gelir, marka doğrudan kopyalayıp CMS'e (HTML/kaynak modunda) yapıştırabilir.

   Use the bundled script:
   ```bash
   python3 /Users/Erdo/.claude/skills/gameplus-category-content/scripts/html_to_docx.py
   ```

3. **(Optional) Excel rollup** — eğer birden fazla kategori üretiyorsan tek Excel dosyasında: URL, HTML (Part 1), HTML (Part 2 — sadece > 32700 chars için), Kategori, Toplam Karakter sütunlarıyla. See `references/excel-export.md`.

## Reference files

- `references/methodology.md` — Yapının arkasındaki SEO + GEO mantığı. Bir kez oku.
- `references/design-system-v10.md` — **GÜNCEL görsel dil (v10.2 "Game+ UI", sarı).** Tüm bileşen HTML/CSS'i buradan. Conic yok, ToC yok.
- `references/ga4-tracking.md` — kategori CTA id'leri (`category-dynamic-cta`, `category-packages-button`) + GTM/GA4 kurulumu.
- `references/structure-template.md` — Bölüm sırası + içerik kuralları (görünüm için design-system-v10.md).
- `references/style-guide.md` — Voice, yasak kelimeler, formatting. Her piece için tekrar oku.
- `references/url-anchor-mapping.md` — URL bazlı anchor text. Link yazmadan önce bak.
- `references/category-pages.md` — Tüm 27 kategori URL ve primary keyword.
- `references/dataforseo-workflow.md` — DataForSEO 8-step sequence.
- `references/checklist.md` — Final QA pass items.
- `references/cta-templates.md` — Fix CTA + Dinamik CTA (C3/C4/D2) şablonları, placeholder'larla.
- `references/excel-export.md` — Bulk Excel rollup formatı.

## Examples

`examples/fps-icerik-v10.html` — **v10.2 referans çıktısı** (FPS kategorisi, v9'dan port edilmiş). Yeni içerik yazarken bunu şablon al.

**Mevcut v9 içeriklerini taşımak için:** `python3 scripts/port_category_v10.py <v9-dosya.html>` — metne DOKUNMAZ, yalnız görsel katman + GA4 id'leri ekler; metnin birebir korunduğunu assert'lerle doğrular.

## What NOT to do

- Blog yazısı tonu kullanma. "Hazır mısın?" gibi rhetorical opener'lar, YouTube embed'ler kategori sayfalarına ait değil.
- Word count'u filler ile şişirme. 2000 hedef floor; her paragraf değerini ödemeli.
- `gameplus.com.tr` dışına link verme. Sadece internal.
- GeForce NOW kütüphanesinde olmayan oyun uydurma. Playwright ile doğrula.
- "buraya tıkla" / "linke tıklayarak" yazma. Anchor'lar keyword-rich phrase.
- Steam Workshop, PEGI yaş etiketleri, spesifik TV model yılları veya Performance vs Ultimate önerisi yazma.
- `/gfn/paketler` body inline link olarak koyma; sadece Fix CTA paketlere gider.
- Dynamic (sayfa-ortası) CTA'yı GFN paketlerine yönlendirme — `/gfn`, `/geforce-now-nedir` veya `/paketler` kullan. `/firsatlar` yasak.
- Hiçbir CTA'da içinde bulunduğun kategori sayfasına self-link verme (xbox içeriğinde `/gfn/oyunlar/xbox`'a link gibi).
- Kütüphane oyun sayısını exact tam sayı yazma (434 değil 400+); her zaman aşağı yuvarlanmış "X+".
- Yeşil `#76b900` veya türevlerini kullanma (v9 kalıntısı); tek vurgu sarı `#FFC900`.
- Callout barını `border-left` ile yapma; ayrı 4px yuvarlak uçlu bar div'i kullan (blog ile birebir).
- `gp-conic` (dönen glow) veya `floating-toc` ekleme.

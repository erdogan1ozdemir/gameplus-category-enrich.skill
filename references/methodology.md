# Gameplus Category Content Methodology

This file explains the *why* behind the structure. Read once when you start using this skill; consult it again when you're unsure why a section exists.

## What makes a Gameplus category page rank

Gameplus GFN category pages compete in a SERP where the top 5 positions are dominated by browser HTML5 game portals (Poki, CrazyGames, Yandex Games) for head terms like "strateji oyunları" or "aksiyon oyunları". These portals satisfy "play now in browser" intent and we can't out-rank them on that intent.

Where Gameplus can win:

1. **Long-tail commercial intent.** "En iyi ücretsiz oyunlar" (33,100 vol, KD 13) is the kind of query where editorial list content out-ranks browser portals. We write category content that doubles as a buyer's guide for the cloud gaming experience.

2. **AI Overviews and ChatGPT citations.** ChatGPT cites Wikipedia, nvidia.com, Webtekno, and a handful of Turkish gaming blogs for "geforce now" queries. We build content that's *quotable* — clear definition sentences, structured comparison tables, named entities — so AI engines pick us as a source.

3. **PAA boxes.** Most game-type queries have a People Also Ask block. Our FAQ section is engineered for those slots — questions worded the way Google's PAA shows them, answers in 40-60 words.

## Five-section content blueprint

Every category page follows the same skeleton because each section does a specific job:

### 1. Definition + value prop intro (150-200 words, 2 paragraphs)

**Job:** Give AI a quotable definition of the category in the first 60 words, then bridge to GeForce NOW's value.

**Why this works:** AI Overviews extract the first definitional sentence of a section. If the first sentence of the page is "Strateji oyunları, oyuncuyu komutan koltuğuna oturtan..." you give Google AI Mode a clean pull-quote. If the first sentence is "GeForce NOW'a hoş geldin!" you give them nothing.

The second paragraph names the actual category sub-types (e.g., RTS, 4X, sıra tabanlı for strategy) and explicitly mentions GAME+ Türkiye servers as the differentiator.

### 2. Popular games table (8-12 rows)

**Job:** Show inventory depth, anchor entity coverage, give scanners a quick "is this category for me" answer.

**Why this works:** Tables are the single most-cited content format in AI Overviews. They're also the section users actually read on category pages — the rest of the article is for SEO and consideration; the table is the conversion driver.

Column structure varies by category but always: Oyun name (with ®/™ marks), Alt Tür, Platform/Erişim Modeli, Öne Çıkan Özellik.

Game selection priorities (in order):
1. Games currently in the live GeForce NOW library (verified from the category grid)
2. Games AI Overviews / ChatGPT mention for adjacent queries
3. Recent or popular releases that haven't been listed in older content
4. Games with strong publisher names that improve E-E-A-T (CD Projekt Red, Paradox, FromSoftware, etc.)

### 3. Cloud gaming advantages bullet list (5-7 items)

**Job:** Convert the SEO visitor into a paying subscriber by explaining *why* cloud gaming solves their actual problem.

**Why this works:** Most users hitting these pages already know what "strateji oyunları" are. They don't need the category explained — they need to understand why playing them on Gameplus is better than installing them locally. Each bullet pairs a real friction point (50+ GB downloads, hardware that can't handle Cyberpunk's ray tracing, hours of updates) with the GeForce NOW solution.

Format: bold lead-in phrase, then 2-3 sentences with a concrete example. Don't write abstract advantages — name the specific games where the advantage matters.

### 4. Sub-genre guide with H4 sub-sections (5-7 H4s, 100-150 words each)

**Job:** Topical authority signal for Google, and a "which sub-genre am I" reader journey.

**Why this works:** A single-H3 category page reads as thin to Google. A category page with 5 well-developed H4 sub-sections covering distinct sub-genres signals topical breadth — this is the same pattern Wikipedia uses on disambiguation pages, and Google rewards it.

For each sub-genre H4, hit this pattern:
- Sentence 1-2: Define the sub-genre mechanically
- Sentence 3-4: Name 1-2 reference games in that sub-genre that are on GeForce NOW
- Sentence 5-6: Why cloud gaming matters for *this specific* sub-genre (e.g., for soulslike: kare hızı kararlılığı, for RTS: girdi gecikmesi, for açık dünya: yükleme süresi)
- Bullet list of 3-5 standout games in that sub-genre

### 5. Technical settings + paket comparison + FAQ + CTA

**Job:** Capture late-funnel intent ("hangi paket bana uygun") and surface in PAA.

The technical settings table answers "ne kadar internet lazım", "hangi controller çalışır" — these are real Turkish search queries that appear in Google Suggest.

The paket comparison table is critical: it's the page's primary internal funnel toward `/gfn/paketler`. Don't half-ass it — list every meaningful Performance vs Ultimate difference (resolution, FPS, session length, DLSS 3, Reflex, Cloud G-Sync). Follow with one paragraph guiding the reader: "tek oyunculu için Performance yeter, rekabetçi için Ultimate al."

FAQ is 4-6 questions, no more. Each question should be different from anything already answered in body text. Common question patterns Google rewards in PAA:
- "GeForce NOW'da kaç tane [tür] oyunu var?"
- "[Tür] oyunlarına yeni başlayanlar hangi oyunla başlamalı?"
- "Çok oyunculu [tür] oyunları bulut üzerinden oynanabilir mi?"

CTA paragraph is 2-3 sentences. Name specific games the reader was just considering, restate the "no powerful PC needed" promise, end with three imperatives: kütüphaneni bağla, paket seç, oynamaya başla.

## SEO vs GEO balance

These pages serve both Google's traditional SERP and AI search engines. Where the two demand different things, we side with GEO because that's where Gameplus has more upside (the SERP is locked up by HTML5 portals; AI Overviews are wide open).

GEO-specific design choices:
- Definition patterns ("X oyunları, ... bir oyun türüdür")
- Self-contained answer blocks of 134-167 words (AI's optimal citation length)
- Named entities consistently across the page (game titles always in `<strong>`)
- Tables with extractable rows (every row reads as a standalone fact)
- Question-as-H4 FAQ format

What we don't do for GEO:
- Keyword stuffing — AI engines down-rank obvious SEO patterns
- Repetitive intros across pages — AI dedupes near-identical phrasing across a domain
- Pure listicle format — AI prefers explanatory prose around lists, not naked lists

## Length target rationale

~2000 words is not arbitrary. It's the median length of content ranking top 10 for "en iyi [tür] oyunları" in Turkish. Shorter content gets out-ranked by editorial guides; longer content (3000+ words) hurts time-on-page and bounces. 1800-2200 is the sweet spot.

If you're below 1700 words after the standard structure, the most likely cause is shallow sub-genre H4s. Each should be 100-150 words. If they're 60 words each, you're writing genre definitions instead of genre experiences — go deeper.

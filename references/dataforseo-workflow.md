# DataForSEO Workflow

The exact MCP tool sequence to run during Phase 2 (research). Follow this in order — each step's output informs the next.

## MCP namespace

DataForSEO MCP tools are exposed under two possible namespaces depending on the user's setup:
- `mcp__dfs-mcp__*` (older naming)
- `mcp__dataforseo__*` (newer naming)

If one is disabled, the other is usually available. Try `mcp__dfs-mcp__kw_data_google_ads_search_volume` first; if you get "tool disabled", switch to the `mcp__dataforseo__` prefix.

If both fail, fall back to delegating the research to an `Agent` subagent which often has access to a working namespace.

## Standard parameters

For every Turkish content piece:
- `location_code`: **2792** (Türkiye)
- `language_code`: **"tr"**
- For SERP tools: `depth`: 20 (gives top 20 results plus SERP features)
- For keyword suggestion tools: `limit`: 30

These are numbers, not strings. Validation errors complaining about "Expected number, received string" usually mean you passed `"2792"` instead of `2792`.

## Step-by-step workflow

### Step 1: Build the candidate keyword list

Before any API call, brainstorm 10-15 candidate keywords for the target category. Always include:

1. **Primary keyword** (from `category-pages.md`, e.g., "strateji oyunları")
2. **"En iyi" variant** (often higher commercial intent and lower KD — e.g., "en iyi strateji oyunları")
3. **"PC" variant** ("strateji oyunları pc")
4. **GeForce NOW-prefixed variant** ("geforce now strateji oyunları")
5. **Free / ücretsiz variant** ("ücretsiz strateji oyunları")
6. **Sub-genre / type variants** (e.g., for strateji: "rts oyunları", "4x strateji oyunları", "sıra tabanlı strateji")
7. **Branded title queries** that overlap with the category (e.g., "civilization", "age of empires" — these surface SERP intent signals)
8. **Cross-keyword variants** for split categories (e.g., for aksiyon: "savaş oyunları" — 33,100 vol/mo, much higher than "aksiyon oyunları")
9. **"Ne", "nasıl" variants** if relevant (informational intent flags)
10. **Year-suffixed variants** ("strateji oyunları 2026") for freshness queries

### Step 2: Search volume + competition

Call `kw_data_google_ads_search_volume`:

```
{
  "keywords": ["strateji oyunları", "en iyi strateji oyunları", "strateji oyunları pc", ...],
  "location_code": 2792,
  "language_code": "tr"
}
```

Returns: monthly search volume, competition level (LOW/MEDIUM/HIGH), CPC, low/high bid, 12-month trend per keyword.

**What to look for:**
- Volumes ≥ 100/mo (anything below is too thin to target on its own)
- LOW competition with high volume (rare but golden — e.g., "savaş oyunları" 33,100 LOW)
- Recent trend rises (signals seasonality or growing interest)

### Step 3: Keyword difficulty

Call `dataforseo_labs_bulk_keyword_difficulty`:

```
{
  "keywords": [<same list as above>],
  "location_code": 2792,
  "language_code": "tr"
}
```

Returns: KD score 0-100 per keyword. Lower = easier to rank.

**What to look for:**
- KD < 20 with volume ≥ 1,000 → highest priority targets
- KD 20-40 with volume ≥ 10,000 → secondary targets (need stronger backlink profile)
- KD > 50 → de-prioritize unless they're branded queries

Some keywords return null/no KD. That's fine — usually means the keyword is so niche that DataForSEO doesn't have a model for it. Use search volume as the primary signal for those.

### Step 4: Search intent classification

Call `dataforseo_labs_search_intent`:

```
{
  "keywords": [<top 8 from your list>],
  "location_code": 2792,
  "language_code": "tr"
}
```

Returns: primary intent (informational / commercial / transactional / navigational) and probability.

**What to look for:**
- **Transactional** → user wants to play/buy; perfect for our cloud gaming positioning
- **Commercial** → user is comparing; FAQ and paket-comparison sections matter
- **Informational** → user wants definitions; intro paragraph matters more
- **Navigational** → user is hunting for a specific brand (e.g., "fortnite"); we won't rank for these but they tell us which entities matter

### Step 5: Long-tail expansion

Call `dataforseo_labs_google_keyword_suggestions`:

```
{
  "keyword": "<primary keyword, singular>",
  "location_code": 2792,
  "language_code": "tr",
  "limit": 30
}
```

Returns: up to 30 related long-tail keywords with their volumes and KDs.

**What to look for:**
- New keyword variants you didn't think of (e.g., "ordu yönetme oyunu pc", "ucretsiz strateji oyunları pc")
- Long-tail with KD < 10 — these become candidates for FAQ questions or H4 sub-section headings
- Branded queries you should mention by name in the body

### Step 6: SERP analysis

Call `serp_organic_live_advanced` on **2-3 top target keywords**:

```
{
  "keyword": "en iyi strateji oyunları",
  "location_code": 2792,
  "language_code": "tr",
  "depth": 20
}
```

Returns: top 20 organic results, plus SERP features (AI Overview, PAA, featured snippets, video pack, related searches).

**What to look for:**
- **Who's ranking?** If top 5 is dominated by browser HTML5 portals (Poki, CrazyGames), the head term has "play now" intent and we should target the "en iyi" / informational variant instead.
- **AI Overview present?** Capture the cited sources — these are our competition for AI citations.
- **PAA questions** → these become our FAQ questions (use the exact wording Google shows).
- **Related searches** at the bottom → long-tail expansion ideas we may have missed.
- **Featured snippet host** (if any) → that's the page to beat for that snippet.

### Step 7: Competitor keyword mining (CRITICAL — do not skip)

This is where most of the long-tail keyword opportunities come from. The flow:

1. After Step 6 (SERP analysis), you should have a clear shortlist of **2-4 target keywords** that fit the category: high volume, manageable KD, intent matches "cloud gaming category page". Lock these in before proceeding.

2. For each of those 2-4 target keywords, take the **top 5 ranking URLs** from the SERP results in Step 6 (exclude pure brand storefronts like Steam/Epic if they show up — they don't share keyword profiles with editorial content).

3. For each competitor URL, call `mcp__dfs-mcp__dataforseo_labs_google_ranked_keywords`:

```
{
  "target": "<competitor URL or domain>",
  "location_code": 2792,
  "language_code": "tr",
  "limit": 100,
  "filters": [["keyword_data.keyword_info.search_volume", ">=", 50]],
  "order_by": ["keyword_data.keyword_info.search_volume,desc"]
}
```

   Pass URL as `target` if you want page-level keyword set. Use `mode: "as_is"` for exact URL or `"subdomains"` for the whole domain.

4. Aggregate all keywords returned across the 5 competitors. Look for:
   - **Keywords appearing on 2+ competitors** → high-confidence opportunity (these are topical must-haves)
   - **Keywords with volume ≥ 100 + KD ≤ 30** that we could realistically rank for
   - **Keywords competitor ranks position 4-15 with decent volume** — they're not dominating either, so it's contestable
   - **Sub-genre and entity keywords** (specific game names with strong volume that we should mention in body)

5. **Pull the harvested keyword set through one final filter:** Drop keywords that conflict with our positioning (e.g., "ücretsiz online oyunlar oyna" leans browser-portal intent; "X oyunu indir" leans direct download — we're a cloud service, not a download portal). Keep the rest.

6. The output of Step 7 is a **"must-use keywords" list of 10-20 terms** — keywords that the competitors are ranking for, that we should integrate into the body via:
   - Sub-genre H4 names
   - Bullet list items
   - FAQ question wording
   - Paragraph text where they fit naturally

This step is what differentiates content that "covers a topic" from content that "owns a topic". The first version of a category page typically targets the obvious 3-4 head terms; competitor mining surfaces the long-tail breadth that gives us topical authority.

**Example outcome for the simulasyon page (real run):**
- Target keywords locked in: simülasyon oyunları (2,900), simulator oyunları (1,600), şehir kurma oyunu (1,300), uçak simülasyon oyunları (1,300, +307% YoY)
- Top 5 competitors mined: crazygames.com/tr/c/sim, oyunskor.com/oyunlar/simulasyon, poki.com/tr/simülasyon, store.epicgames.com/tr/c/simulation-games, yandex.com.tr/games/kategori/simulator
- Must-use keywords surfaced from mining: araba simülasyon oyunları pc (90), yaşam simülasyon oyunları (50), çiftlik simülasyonu, futbol menajerlik simülasyonu (90 — but careful, no Football Manager in GFN library), tren simülasyonu, otobüs simülatörü, koloni oyunu, fabrika simülatörü, hastane yönetim oyunu, ortaçağ şehir simülasyonu
- These directly informed the body: H4 sub-genres (yaşam/çiftlik, koloni/üretim), bullet list items (Train Sim World 5, Bus Simulator 21, Construction Simulator), and paragraph entity mentions

### Step 8 (optional but recommended): ChatGPT citation check

Call `ai_optimization_chat_gpt_scraper`:

```
{
  "keyword": "en iyi strateji oyunları geforce now",
  "location_name": "Turkiye",   <-- "Turkiye" not "Turkey"
  "language_code": "tr"
}
```

Returns: what ChatGPT web search returns for the query — the response text, cited domains, and brand entities (game titles) ChatGPT mentions.

**What to look for:**
- **Cited domains** → who is currently in ChatGPT's knowledge base for this topic? (Often nvidia.com, webtekno.com, donanimhaber.com for Turkish gaming queries.)
- **Brand entities ChatGPT lists** → these are games we should consider including in our table. ChatGPT's selection reflects what's prominent on the web; missing one of their picks signals a coverage gap.
- **Gameplus visibility** → if gameplus.com.tr is *not* cited, that confirms an opportunity. If it is, see which URL is being cited and don't cannibalize.

## What to do with the data

After all 7 steps, you should have:

- **3-5 prioritized target keywords** for the page (one primary + 2-4 secondaries)
- **Volume + KD context** for each
- **A list of FAQ questions** drawn from PAA + low-volume long-tails
- **A list of must-mention game entities** drawn from AI Overview + ChatGPT citations + SERP-ranking content
- **A clear sense of intent** that informs which sections to emphasize

Summarize these in 5-10 lines and use them to inform the actual writing in Phase 3-4.

## Cost awareness

These tools are billed per call. Rough costs:
- `kw_data_google_ads_search_volume`: $0.05 per batch (any number of keywords in one call)
- `dataforseo_labs_bulk_keyword_difficulty`: $0.01
- `dataforseo_labs_search_intent`: $0.05
- `dataforseo_labs_google_keyword_suggestions`: $0.05
- `serp_organic_live_advanced`: $0.002 per 100 results × 2-3 queries = ~$0.01
- `ai_optimization_chat_gpt_scraper`: $0.05

Total per content piece: ~$0.20. Don't run the same call twice in a session — cache mentally.

## Fallbacks

If DataForSEO is completely unavailable:

1. Use the live SERP via Playwright: navigate to `https://www.google.com.tr/search?q=<keyword>` and capture the top 10 results + PAA.
2. Use the ChatGPT API or browser to manually check what comes up for the target query.
3. Use keyword research the user supplies in chat.

Document in the content brief that DataForSEO data was unavailable so the user knows the keyword strategy is based on manual signals.

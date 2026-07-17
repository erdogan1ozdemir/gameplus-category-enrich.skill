# GA4 Tıklama Takibi — Kategori CTA id'leri

Kategori gövdesindeki CTA butonları **sabit `id`** taşır; id'ler her kategoride aynıdır, tek GTM kuralı 27 kategoriyi birden kapsar.

| `id` | Blok | Hedef |
|---|---|---|
| `category-dynamic-cta` | Sayfa ortası dinamik CTA | `/gfn` \| `/geforce-now-nedir` \| `/firsatlar` (kategoriler arası rotasyon) |
| `category-packages-button` | Fix CTA (sayfa sonu) | `/gfn/paketler` |

**Neden önemli:** dinamik CTA rotasyonlu olduğu için hangi hedefin daha çok tıklandığını ancak bu id + `cta_url` kırılımıyla ölçebiliriz.

## GTM kurulumu
1. **Değişken:** yerleşik `Click ID` aktif.
2. **Tetikleyici:** Click - Just Links → *Some Link Clicks* → Click ID `matches RegEx`:
   ```
   ^(category-dynamic-cta|category-packages-button)$
   ```
3. **Etiket:** GA4 Event `category_cta_click`, parametreler: `cta_id`={{Click ID}}, `cta_url`={{Click URL}}, `cta_text`={{Click Text}}, `page_location`={{Page URL}}.
4. **GA4:** Admin → Custom definitions'ta `cta_id` / `cta_url` / `cta_text` custom dimension olarak tanımlanmalı.

Blog tarafındaki eşdeğeri `blog_cta_click`; ikisi ayrı event adı kullanır ki rapor kırılımı temiz olsun.

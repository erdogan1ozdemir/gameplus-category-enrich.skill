# CTA Templates (v9 koyu — V9 Layered Frame)

> **v10.2:** Görsel dil `design-system-v10.md`'dedir (sarı `#FFC900`, `#161616` kart, dolu butonda `#131313` metin).
> **GA4 id'leri ZORUNLU:** dinamik (sayfa-ortası) CTA butonuna `id="category-dynamic-cta"`, Fix CTA butonuna `id="category-packages-button"`. Bkz. `ga4-tracking.md`.

Two CTAs appear in every category content:

1. **Fix CTA** — same across all 27 categories, placed just before the final paragraph
2. **Dynamic CTA** — category-specific, placed after the avantajlar list (mid-article)

**CTA link kuralı (GÜNCEL — Gameplus revizyonu):**
- **Fix CTA (alt)** → `https://gameplus.com.tr/gfn/paketler`. Bu, dönüşümün gerçekleştiği TEK paketler linkidir.
- **Dynamic CTA (sayfa ortası)** → paketlere DEĞİL, şu 3 sayfadan birine yönlendirir (çeşitlilik için kategoriler arasında rotasyon yap): `https://gameplus.com.tr/gfn` (GFN ana sayfa), `https://gameplus.com.tr/geforce-now-nedir` (Nasıl Çalışır / GFN nedir), `https://gameplus.com.tr/firsatlar` (Fırsatlar).
- **Hiçbir CTA, içinde bulunduğu kategori sayfasının kendisine link VERMEZ** (self-link yasak). Örn. xbox içeriğinin CTA'sı `/gfn/oyunlar/xbox`'a link vermez.
- **No `/gfn/paketler` inline link in body** — sadece Fix CTA paketlere gider.

### Sayfa-ortası (Dynamic) CTA hedefleri

| Hedef URL | Buton metni örneği |
|---|---|
| `https://gameplus.com.tr/gfn` | `GeForce NOW'u Keşfet →` |
| `https://gameplus.com.tr/geforce-now-nedir` | `GeForce NOW Nasıl Çalışır? →` |
| `https://gameplus.com.tr/firsatlar` | `GeForce NOW Fırsatları →` |

D2 (çift buton) kullanılıyorsa iki buton, bu 3 hedeften **birbirinden farklı** ikisine gider (biri paketlere veya kategorinin kendisine DEĞİL).

> **v9 GÜNCEL:** Tüm CTA'lar saf siyah `#000` zemin + **V9 Layered Frame** (`gp-card`: soluk yeşil dış + çok soluk iç çerçeve). **Rotating conic glow KULLANILMAZ** (blog skill'inden farkı budur). `gp-card` sınıfı `design-system-v9.md`'deki paylaşılan `<style>` bloğunu gerektirir — body'nin başına bir kez ekle.

## Fix CTA (sabit)

Always the same. Update only the button text or headline if Gameplus team revises.

```html
<div class="gp-card" style="--gp-frame:rgba(255,201,0,0.30);color:#fff;padding:24px 28px;margin:32px 0;box-shadow:0 6px 24px rgba(0,0,0,0.55);">
  <div style="display:flex;align-items:center;gap:14px;margin-bottom:16px;flex-wrap:wrap;">
    <div style="font-size:1.15em;font-weight:800;color:#fff;letter-spacing:-0.01em;">
      GeForce <span style="color:#FFC900;">NOW</span>
    </div>
    <div style="height:18px;width:1px;background:#2a2a2a;"></div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;">
      <span style="color:#FFC900;font-weight:700;font-size:0.7em;padding:4px 10px;border:1px solid #FFC900;border-radius:4px;letter-spacing:0.1em;text-transform:uppercase;">Performance</span>
      <span style="color:#FFC900;font-weight:700;font-size:0.7em;padding:4px 10px;border:1px solid #FFC900;border-radius:4px;letter-spacing:0.1em;text-transform:uppercase;">Ultimate</span>
    </div>
  </div>
  <div style="font-size:1.32em;font-weight:800;margin-bottom:6px;line-height:1.3;letter-spacing:-0.015em;">Tek üyelik, hazır kütüphane.</div>
  <p style="color:#B2B2B2;margin:0 0 18px 0;line-height:1.55;font-size:0.95em;">Performance ve Ultimate paketleri kütüphanendeki oyunları çalıştırır. Steam, Epic Games, EA App, Xbox ve Ubisoft Connect hesapları bağlanabilir.</p>
  <a class="gp-cta-btn" href="https://gameplus.com.tr/gfn/paketler" style="display:inline-flex;align-items:center;background:#FFC900;color:#131313;padding:12px 16px;border-radius:8px;font-weight:700;font-size:16px;line-height:20px;text-decoration:none;">GeForce NOW Paketlerini İncele &rarr;</a>
</div>
```

Karakteristikler:
- `#000` siyah zemin + V9 layered frame (soluk yeşil çerçeve)
- "GeForce" beyaz, "NOW" NVIDIA yeşili (`#FFC900`)
- PERFORMANCE / ULTIMATE bordered kapsül etiketler (uppercase via CSS)
- Headline: "Tek üyelik, hazır kütüphane."
- Buton: "GeForce NOW Paketlerini İncele →"

## Dynamic CTA (kategori bazlı)

3 stil var. Kategoriye en uygunu seç:

| Stil | Ne zaman kullan | Örnek kategoriler |
|---|---|---|
| **C3** Badge + Headline | Hikaye anlatımı güçlü, somut oyunlar var | Simülasyon, FPS, MMO, RPG, Aile Dostu |
| **C4** Stat Banner | Sayısı etkileyici (büyük/küçük/0₺) | Strateji (600+), F2P (350+), İndie (900+), MOBA (10+) |
| **D2** Dual Button | Mağaza/platform; ikinci yönlendirme yolu mantıklı | Steam, Epic Games, Xbox, Aksiyon |

> **C4 sayıları:** kütüphane boyutu stat'ı her zaman yuvarlanmış "X+" yazılır (616 → 600+, 14 → 10+). Bkz. design-system-v9.md "Sayı yuvarlama".

### C3 — Badge + Headline

```html
<div class="gp-card" style="--gp-frame:rgba(255,201,0,0.22);color:#fff;padding:22px 24px;margin:24px 0;box-shadow:0 4px 18px rgba(0,0,0,0.5);">
  <div style="display:inline-block;color:#FFC900;font-size:12px;line-height:16px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:12px;display:inline-flex;align-items:center;">{{BADGE}}</div>
  <div style="font-weight:800;font-size:1.18em;margin-bottom:6px;letter-spacing:-0.01em;">{{HEADLINE}}</div>
  <div style="color:#B2B2B2;font-size:0.93em;margin-bottom:16px;line-height:1.55;">{{DESC}}</div>
  <a class="gp-cta-btn" href="{{MID_CTA_URL}}" style="display:inline-flex;align-items:center;background:#FFC900;color:#131313;padding:12px 16px;border-radius:8px;font-weight:700;font-size:16px;line-height:20px;text-decoration:none;">{{MID_CTA_LABEL}} &rarr;</a>
</div>
```

Placeholders:
- `{{BADGE}}` — Kategori adı uppercase (örn. "FPS", "AİLE DOSTU", "STRATEJİ")
- `{{HEADLINE}}` — Kategoriye özel 1 cümle hook (somut oyun isimleri)
- `{{DESC}}` — 1-2 cümle context (gecikme stat'ı, FPS, vs.)
- `{{MID_CTA_URL}}` / `{{MID_CTA_LABEL}}` — yukarıdaki "Sayfa-ortası CTA hedefleri" tablosundan biri (paketler DEĞİL, self DEĞİL)

Örnek (FPS):
- BADGE: `FPS`
- HEADLINE: `Counter-Strike 2 ranked maçlarında zamanı yakala.`
- DESC: `Battlefield 2042, Apex Legends, R6 Siege X; Türkiye sunucularıyla 40 ms gecikme rekabetçi maçlarda fark yaratır.`

### C4 — Stat Banner

```html
<div class="gp-card" style="--gp-frame:rgba(255,201,0,0.22);color:#fff;padding:20px 24px;display:flex;flex-wrap:wrap;gap:24px;align-items:center;justify-content:space-between;margin:24px 0;box-shadow:0 4px 18px rgba(0,0,0,0.5);">
  <div style="display:flex;gap:28px;flex-wrap:wrap;">
    <div>
      <div style="font-size:1.8em;font-weight:800;color:#FFC900;line-height:1;">{{NUM1}}</div>
      <div style="font-size:0.7em;color:#a8b2c0;text-transform:uppercase;letter-spacing:0.12em;margin-top:5px;font-weight:700;">{{LABEL1}}</div>
    </div>
    <div>
      <div style="font-size:1.8em;font-weight:800;color:#FFC900;line-height:1;">{{NUM2}}</div>
      <div style="font-size:0.7em;color:#a8b2c0;text-transform:uppercase;letter-spacing:0.12em;margin-top:5px;font-weight:700;">{{LABEL2}}</div>
    </div>
  </div>
  <a class="gp-cta-btn" href="{{MID_CTA_URL}}" style="background:#FFC900;color:#fff;padding:11px 24px;border-radius:6px;font-weight:700;text-decoration:none;white-space:nowrap;box-shadow:0 2px 8px rgba(255,201,0,0.35);">{{MID_CTA_LABEL}} &rarr;</a>
</div>
```

Placeholders (2 stat):
- `{{NUM1}}`, `{{LABEL1}}` — birinci sayı + etiket (örn. "600+" + "Strateji Oyunu")
- `{{NUM2}}`, `{{LABEL2}}` — ikinci sayı + etiket (örn. "5" + "Alt Tür")
- `{{MID_CTA_URL}}` / `{{MID_CTA_LABEL}}` — sayfa-ortası hedef tablosundan (paketler DEĞİL)

Örnek (Strateji): NUM1=**600+** / LABEL1=Strateji Oyunu, NUM2=5 / LABEL2=Alt Tür. **Not:** stat sayısı kütüphane boyutuysa exact değil yuvarlanmış "X+" yaz (616 değil 600+).

### D2 — Dual Button

```html
<div class="gp-card" style="--gp-frame:rgba(255,201,0,0.22);color:#fff;padding:22px 24px;margin:24px 0;box-shadow:0 4px 18px rgba(0,0,0,0.5);">
  <div style="font-weight:800;font-size:1.12em;margin-bottom:6px;letter-spacing:-0.01em;">{{HEADLINE}}</div>
  <div style="color:#B2B2B2;font-size:0.93em;margin-bottom:14px;line-height:1.55;">{{DESC}}</div>
  <div style="display:flex;flex-wrap:wrap;gap:10px;">
    <a class="gp-cta-btn" href="{{BTN1_URL}}" style="background:#FFC900;color:#fff;padding:10px 22px;border-radius:6px;font-weight:700;text-decoration:none;font-size:0.95em;box-shadow:0 2px 8px rgba(255,201,0,0.35);">{{BTN1_LABEL}}</a>
    <a class="gp-cta-btn" href="{{BTN2_URL}}" style="background:transparent;color:#fff;padding:9px 21px;border-radius:6px;font-weight:700;text-decoration:none;font-size:0.95em;border:1px solid rgba(255,255,255,0.25);">{{BTN2_LABEL}}</a>
  </div>
</div>
```

Placeholders:
- `{{HEADLINE}}` — 1 cümle
- `{{DESC}}` — 1-2 cümle
- `{{BTN1_URL}}` / `{{BTN1_LABEL}}` — sayfa-ortası hedef tablosundan biri
- `{{BTN2_URL}}` / `{{BTN2_LABEL}}` — tablodan **farklı** ikinci hedef. **ASLA kategori sayfasının kendisi (self-link) veya paketler DEĞİL.**

Örnek (Steam):
- HEADLINE: `Steam hesabını bağla, oyunlarına anında eriş.`
- DESC: `Sahip olduğun 1.500+ Steam yapımı hesabı bağladığın an kütüphanende görünür.`
- BTN1_URL: `https://gameplus.com.tr/gfn` / BTN1_LABEL: `GeForce NOW'u Keşfet`
- BTN2_URL: `https://gameplus.com.tr/firsatlar` / BTN2_LABEL: `GeForce NOW Fırsatları`

## Yazım kuralı (CTA copy)

- Kısa, somut, oyun ismi geçen cümleler kur.
- "Buluta taşı", "anında erişim sağlar" gibi yapay/translated cümlelerden kaçın.
- Mümkünse spesifik bir stat veya gerçek bilgi (40 ms gecikme, 600+ oyun, ücretsiz) ekle.
- Buton metni: Fix CTA'da "GeForce NOW Paketlerini İncele →" (paketlere gider). Dynamic CTA'da hedefe uygun metin: "GeForce NOW'u Keşfet →" (/gfn), "GeForce NOW Nasıl Çalışır? →" (/geforce-now-nedir) veya "GeForce NOW Fırsatları →" (/firsatlar). Dynamic CTA ASLA paketlere veya kategorinin kendisine gitmez.

## Konum

- **Dynamic CTA**: Avantajlar listesinden (Bulutta Oynamanın Avantajları H3) hemen sonra. Lisans callout ondan hemen sonra gelir.
- **Fix CTA**: Final CTA paragrafından (örn. "Strateji Dünyasına Hemen Adım At" H3 ve altındaki paragraf) hemen önce.

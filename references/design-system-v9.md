# Görsel Tasarım Sistemi v9 (Koyu Tema — Kategori)

Bu, kategori içeriklerinin **güncel görsel dilidir**. Blog skill'inin (gameplus-blog-enrich) v9 tasarımıyla aynı premium koyu temadır, **iki fark dışında:**
- **V8 rotating conic glow KULLANILMAZ.** O tarz vurgu gereken yerlerde **V9 Layered Frame** kullan.
- **Floating ToC (İçindekiler) EKLENMEZ.** Kategori sayfaları utility sayfasıdır.

Site zaten koyu temalı olduğu için bloklar **kendi siyahını basmaz; zemin `transparent`** bırakılır (bloklar siteyle kaynaşır, siyah-üstüne-siyah uyumsuzluğu olmaz). Yalnızca **V9 Layered Frame** soluk çerçevesi + içerik görünür. Eski açık tema `#fff`/`#f8f9fa` snippet'lerini KULLANMA.

## 0. Paylaşılan stil bloğu (bir kez, body'nin EN BAŞINA)

Kategori içeriği CMS'e body HTML olarak yapıştırılır. `gp-layer`'ın iç çerçevesi ve FAQ nabzı pseudo-element + keyframe gerektirir; bunlar inline olamaz. Bu yüzden tek bir `<style>` bloğu en başa eklenir (blog skill'inde de bu yapıldı, canlıda sorunsuz çalıştı):

```html
<style>
@keyframes gp-pulse-plus { 0%,100%{transform:scale(1);opacity:1;} 50%{transform:scale(1.18);opacity:0.85;} }
/* V9 Layered Frame: soluk renkli dış + çok soluk iç çerçeve */
.gp-layer { position:relative; border-radius:12px; border:1px solid var(--gp-frame,rgba(118,185,0,0.22)); background:transparent; }
.gp-layer::before { content:''; position:absolute; inset:5px; border:1px solid rgba(255,255,255,0.04); border-radius:8px; pointer-events:none; }
.gp-layer > * { position:relative; z-index:1; }
/* info-card mini hücre çerçevesi (her badge'in etrafı) */
.gp-cell { position:relative; border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px 16px; }
/* Tablo: tek temiz çerçeve + son satır ayracı (alt açık kalmasın), köşeleri yuvarla */
.gp-table-wrap { border:1px solid rgba(118,185,0,0.38); }
.gp-table-wrap.gp-layer::before { display:none; }
.gp-table-wrap table { border-radius:12px; }
.gp-table-wrap tbody tr:last-child td { border-bottom:1px solid rgba(255,255,255,0.06) !important; }
/* FAQ + nabız */
.faq-item .faq-icon { animation: gp-pulse-plus 2.2s ease-in-out infinite; display:inline-flex; align-items:center; justify-content:center; width:22px; height:22px; flex-shrink:0; color:#fbbf24; font-size:1.5em; font-weight:300; line-height:1; }
.faq-item[open] .faq-icon { transform:rotate(45deg); color:#76b900; }
.faq-item summary::-webkit-details-marker { display:none; }
.faq-item summary::marker { display:none; }
/* ===== Mobil responsive (v10) ===== */
@media (max-width:700px) {
  /* Tablolar: yatay kaydırma yok, tüm sütunlar sığar, okunur punto */
  .gp-table-wrap > div { overflow-x:visible !important; }
  .gp-table-wrap table { font-size:0.76em !important; table-layout:fixed; width:100% !important; }
  .gp-table-wrap th, .gp-table-wrap td { padding:8px 7px !important; white-space:normal !important; word-break:break-word; overflow-wrap:anywhere; vertical-align:top; line-height:1.4 !important; }
  .gp-table-wrap th { letter-spacing:0.04em !important; }
  /* Info-card: 2 sütun */
  .info-card { grid-template-columns:repeat(2,1fr) !important; gap:10px !important; }
  /* FAQ: soru + cevap sola dayalı */
  .faq-item summary { padding:13px 13px !important; gap:9px !important; }
  .faq-item .faq-a { padding:12px 14px 15px 14px !important; }
  /* TLDR: kompakt */
  .tldr-block { padding:15px 16px !important; }
  /* CTA: butonlar tam genişlik */
  .gp-cta-btn { width:100% !important; justify-content:center !important; box-sizing:border-box; text-align:center; }
}
</style>
```

## Renk paleti
Zemin **transparent** (site zaten `#000`; bloklara ekstra siyah arka plan BASMA) · metin `#cbd5e1` · **doküman başlığına renk ATAMA** (CMS verir; aşağıdaki `#fff` yalnız simülasyon) · soluk metin `#a8b2c0` (eski #8b95a7'ten bir tık beyaza yakın) · GFN yeşili `#76b900` · açık yeşil `#a3e635` · amber `#f59e0b` · sarı `#fbbf24` · editör mavi `#3b82f6`/`#93c5fd` · çerçeve `#1f1f1f`.
Tür etiketi gerekiyorsa mümkünse GFN kategorisini yaz (Aksiyon, Macera, Strateji, Canlandırma/RPG, FPS, Platform vb.; birden fazla türe uyuyorsa Aksiyon-Macera gibi). Türkçesi yaygınsa Türkçe (KORKU, GİZLİLİK, YARIŞ); JRPG/FPS/SOULSLIKE/ROGUELIKE/INDIE/MOBA terim olarak kalır.

## 1. TLDR — Hızlı Özet (V9 layered, yeşil ✓ maddeler)

```html
<div class="tldr-block gp-layer" style="--gp-frame:rgba(118,185,0,0.30);padding:18px 22px;margin:24px 0;box-shadow:0 2px 12px rgba(0,0,0,0.4);">
  <h3 style="margin:0 0 12px 0;font-size:1.05em;font-weight:800;display:flex;align-items:center;gap:8px;color:#76b900;">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#76b900" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
    <span style="color:#fff;">Hızlı Özet</span>
  </h3>
  <ul style="margin:0;padding:0;list-style:none;color:#cbd5e1;">
    <li style="display:flex;gap:11px;margin:8px 0;align-items:flex-start;line-height:1.5;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#76b900" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;margin-top:3px;"><polyline points="20 6 9 17 4 12"/></svg><span><strong style="color:#f3f4f6;">Kütüphane:</strong> [N] [kategori] oyunu; [kısa tür açıklaması].</span></li>
    <li style="display:flex;gap:11px;margin:8px 0;align-items:flex-start;line-height:1.5;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#76b900" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;margin-top:3px;"><polyline points="20 6 9 17 4 12"/></svg><span><strong style="color:#f3f4f6;">Öne Çıkan Yapımlar:</strong> <em>[Game1]</em>, <em>[Game2]</em>, <em>[Game3]</em>.</span></li>
    <li style="display:flex;gap:11px;margin:8px 0;align-items:flex-start;line-height:1.5;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#76b900" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;margin-top:3px;"><polyline points="20 6 9 17 4 12"/></svg><span><strong style="color:#f3f4f6;">Alt Türler:</strong> [Sub1], [Sub2], [Sub3], [Sub4].</span></li>
    <li style="display:flex;gap:11px;margin:8px 0;align-items:flex-start;line-height:1.5;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#76b900" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;margin-top:3px;"><polyline points="20 6 9 17 4 12"/></svg><span><strong style="color:#f3f4f6;">[4. Özellik]:</strong> [kategoriye özel ek özellik].</span></li>
  </ul>
</div>
```

## 2. Info-Card (4 badge, koyu premium grid)

Dış kapsayıcı çerçevesizdir (şeffaf grid); **her badge kendi soluk `gp-cell` çerçevesini** alır.

```html
<div class="info-card" role="complementary" style="margin:20px 0 28px;display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;">
  <div class="gp-cell">
    <span style="display:block;font-size:0.62em;color:#76b900;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:5px;font-weight:800;">Kütüphane Boyutu</span>
    <span style="font-size:1.05em;font-weight:700;color:#fff;">[N+] Oyun</span>
  </div>
  <div class="gp-cell">
    <span style="display:block;font-size:0.62em;color:#76b900;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:5px;font-weight:800;">Öne Çıkan Yapım</span>
    <span style="font-size:1.05em;font-weight:700;color:#fff;">[Featured Game]</span>
  </div>
  <div class="gp-cell">
    <span style="display:block;font-size:0.62em;color:#76b900;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:5px;font-weight:800;">[Badge 3 Label]</span>
    <span style="font-size:1.05em;font-weight:700;color:#fff;">[Badge 3 Value]</span>
  </div>
  <div class="gp-cell">
    <span style="display:block;font-size:0.62em;color:#76b900;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:5px;font-weight:800;">[Badge 4 Label]</span>
    <span style="font-size:1.05em;font-weight:700;color:#fff;">[Badge 4 Value]</span>
  </div>
</div>
```
Badge 3/4 önerileri ve yasaklar `structure-template.md`'deki ile aynı (Türkiye Sunucusu / PEGI / Önerilen Paket / Mod YASAK).

### Sayı yuvarlama (ZORUNLU)

Kütüphane oyun sayısı **her zaman aşağı yuvarlanmış "X+" biçiminde** yazılır; asla exact tam sayı (Gameplus revizyonu). Aynı değeri badge + TLDR + gövde + FAQ + C4 stat'ında tutarlı kullan.

| Canlı sayı | Yaz | Kural |
|---|---|---|
| 434 | **400+** | ≥100 → en yakın 100 aşağı |
| 921 | **900+** | ≥100 → en yakın 100 aşağı |
| 69 | **60+** | <100 → en yakın 10 aşağı |
| 14 | **10+** | <100 → en yakın 10 aşağı |

Neden: exact sayı yapay görünür ve kütüphane büyüdükçe bayatlar; "X+" hem doğal hem kalıcıdır.

## 3. Tablolar (V9 layered, zebra, yumuşak çerçeve)

Tüm tablolar (popüler oyunlar, teknik, paket) bu sarmalı kullanır:

```html
<div class="gp-table-wrap gp-layer" style="--gp-frame:rgba(118,185,0,0.22);margin:22px 0;box-shadow:0 4px 18px rgba(0,0,0,0.5);overflow:hidden;">
  <div style="overflow-x:auto;">
    <table style="width:100%;border-collapse:collapse;background:transparent;font-size:0.93em;">
      <thead><tr>
        <th style="padding:14px 18px;text-align:left;border-bottom:1px solid rgba(118,185,0,0.18);font-weight:800;color:#76b900;font-size:0.98em;letter-spacing:0.06em;text-transform:uppercase;">Oyun</th>
        <th style="padding:14px 18px;text-align:left;border-bottom:1px solid rgba(118,185,0,0.18);font-weight:800;color:#76b900;font-size:0.98em;letter-spacing:0.06em;text-transform:uppercase;">Alt Tür</th>
        <th style="padding:14px 18px;text-align:left;border-bottom:1px solid rgba(118,185,0,0.18);font-weight:800;color:#76b900;font-size:0.98em;letter-spacing:0.06em;text-transform:uppercase;">Platform</th>
        <th style="padding:14px 18px;text-align:left;border-bottom:1px solid rgba(118,185,0,0.18);font-weight:800;color:#76b900;font-size:0.98em;letter-spacing:0.06em;text-transform:uppercase;">Öne Çıkan Özellik</th>
      </tr></thead>
      <tbody>
        <tr><td style="padding:11px 18px;vertical-align:top;border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);color:#cbd5e1;line-height:1.5;"><strong style="color:#f3f4f6;">[Game]</strong></td><td style="padding:11px 18px;vertical-align:top;border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);color:#cbd5e1;">[Alt Tür]</td><td style="padding:11px 18px;vertical-align:top;border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);color:#cbd5e1;">[Platform]</td><td style="padding:11px 18px;vertical-align:top;border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);color:#cbd5e1;line-height:1.5;">[Özellik]</td></tr>
        <!-- Tek satırlarda background kaldır (zebra). Son satırda border-bottom yok (CSS hallediyor). -->
      </tbody>
    </table>
  </div>
</div>
```
Zebra: çift sıralı satırlarda `background:rgba(255,255,255,0.015)`, tek sıralarda kaldır. Oyun adı her zaman `<strong style="color:#f3f4f6;">`. Yaş kolonu YOK.

## 4. Editör Notu (V9 layered, mavi)

```html
<div class="editor-note gp-layer" style="--gp-frame:rgba(59,130,246,0.22);padding:14px 18px;margin:22px 0;box-shadow:0 2px 12px rgba(0,0,0,0.4);">
  <div style="display:flex;align-items:center;gap:8px;font-weight:800;margin-bottom:6px;color:#93c5fd;font-size:0.72em;letter-spacing:0.12em;text-transform:uppercase;">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#93c5fd" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>Game+ Editör Notu
  </div>
  <p style="margin:0;color:#cbd5e1;line-height:1.6;font-size:0.94em;">[Faktüel ek bilgi. Yaş/PEGI/yıl iddiası YOK.]</p>
</div>
```

## 5. Lisans Callout / Hatırlatma (V9 layered, amber)

```html
<div class="callout gp-layer" style="--gp-frame:rgba(245,158,11,0.22);padding:14px 18px;margin:22px 0;box-shadow:0 2px 12px rgba(0,0,0,0.4);">
  <div style="display:flex;align-items:center;gap:8px;font-weight:800;margin-bottom:6px;color:#fbbf24;font-size:0.72em;letter-spacing:0.12em;text-transform:uppercase;">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M15.09 14a5 5 0 1 0-6.18 0c.66.49 1.09 1.27 1.09 2.1V17h4v-.9c0-.83.43-1.61 1.09-2.1z"/></svg>Hatırlatma
  </div>
  <p style="margin:0;color:#fde68a;line-height:1.6;font-size:0.94em;">GeForce NOW oyun satmaz; mevcut Steam, Epic Games Store, Xbox, EA App veya Ubisoft Connect kütüphanendeki lisansları bulut üzerinden çalıştırır. [Kategori] oynamak için ilgili platformda oyuna sahip olman gerekir.</p>
</div>
```

## 6. FAQ Accordion (nabız atan +, koyu)

```html
<div class="faq-block" style="margin:24px 0;">
  <details class="faq-item" style="margin-bottom:10px;border:1px solid #1f1f1f;border-radius:10px;overflow:hidden;background:transparent;box-shadow:0 2px 8px rgba(0,0,0,0.4);">
    <summary class="faq-q" style="display:flex;align-items:center;gap:14px;padding:16px 20px;cursor:pointer;background:transparent;font-weight:700;color:#f3f4f6;list-style:none;letter-spacing:-0.005em;">
      <span class="faq-icon">+</span>
      <span style="flex:1;">[Soru — direkt summary içinde, h4 wrap YOK]</span>
    </summary>
    <div class="faq-a" style="padding:14px 20px 18px 56px;border-top:1px solid #1f1f1f;background:transparent;">
      <p style="margin:0;color:#cbd5e1;line-height:1.6;font-size:0.94em;">[Cevap. 40-60 kelime.]</p>
    </div>
  </details>
  <!-- 4-6 soru -->
</div>
```

## 7. CTA'lar
Tüm CTA snippet'leri (Fix + Dynamic C3/C4/D2) için `cta-templates.md`'nin **v9 koyu sürümlerini** kullan. Hepsi V9 layered frame (`gp-layer`), şeffaf zemin, **conic YOK**.

**Link kuralı:** Fix CTA → `/gfn/paketler`. Dynamic (sayfa-ortası) CTA → `/gfn` | `/geforce-now-nedir` | `/firsatlar` (paketler DEĞİL, kategori self-link DEĞİL). Detay: `cta-templates.md`.

## Eşleme özeti (eski açık → yeni v9 koyu)
| Bileşen | Eski | v9 |
|---|---|---|
| TLDR | `#f8f9fa` açık | şeffaf + V9 layer + yeşil ✓ |
| Info-card | `#fff` açık | şeffaf + her hücre gp-cell çerçeve |
| Tablo | `#fff` + `#e5e7eb` | şeffaf + V9 layer + zebra + yeşil th |
| Editör notu | `#eef6ff` açık mavi | şeffaf + V9 layer mavi |
| Lisans callout | `#fef3c7` açık sarı | şeffaf + V9 layer amber |
| FAQ | `#f9fafb` açık | şeffaf + nabız `+` |
| CTA (fix/dynamic) | `#0f172a` navy | şeffaf + V9 layer |
| Conic glow | — | KULLANMA |
| Floating ToC | — | EKLEME |

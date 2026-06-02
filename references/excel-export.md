# Excel Rollup Export

Birden fazla kategori içeriği aynı anda üretildiğinde, hepsini tek Excel dosyasında toplamak için kullanılır. CMS toplu paste için pratik.

## Excel Yapısı

| Sütun | İçerik |
|---|---|
| **A** — URL | Sayfa URL'si (gameplus.com.tr/gfn/oyunlar/...) |
| **B** — HTML (Part 1) | Body HTML, minified, 32700 chars'a kadar |
| **C** — HTML (Part 2) | Sadece HTML 32700'ü aşıyorsa kullanılır |
| **D** — Kategori | Kategori key (strateji, aksiyon, vb.) |
| **E** — Toplam Karakter | Minified HTML uzunluğu |

Excel hücre limiti **32,767 karakter**. Daha uzun HTML'leri iki hücreye split etmek gerekir.

## Python Script Pattern

```python
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
import re

EXCEL_CELL_LIMIT = 32700  # safe margin

def minify_html(html):
    """Aggressive minification: remove comments, collapse whitespace, strip style attribute spaces."""
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    html = re.sub(r'>\s+<', '><', html)
    def strip_style(m):
        s = m.group(1)
        s = re.sub(r'\s*:\s*', ':', s)
        s = re.sub(r'\s*;\s*', ';', s)
        s = re.sub(r',\s+', ',', s)
        return f'style="{s.strip()}"'
    html = re.sub(r'style="([^"]*)"', strip_style, html)
    html = re.sub(r'  +', ' ', html)
    html = re.sub(r'\n\s+', '\n', html)
    html = re.sub(r'\n{2,}', '\n', html)
    return html.strip()

wb = Workbook()
ws = wb.active
ws.title = "Gameplus Kategori İçerikleri"

# Header
ws['A1'] = 'URL'
ws['B1'] = 'HTML (Part 1)'
ws['C1'] = 'HTML (Part 2 - boşsa Part 1 tek başına)'
ws['D1'] = 'Kategori'
ws['E1'] = 'Toplam Karakter'
for col in ['A1','B1','C1','D1','E1']:
    ws[col].font = Font(bold=True, size=11)

# Data rows
for i, (url, html, key) in enumerate(results, start=2):
    minified = minify_html(html)
    ws.cell(row=i, column=1, value=url)
    if len(minified) <= EXCEL_CELL_LIMIT:
        ws.cell(row=i, column=2, value=minified)
        ws.cell(row=i, column=3, value='')
    else:
        mid = len(minified) // 2
        split_match = re.search(r'>(?!.*?>)', minified[mid:mid+5000])
        split = mid + (split_match.end() if split_match else 0)
        if split == 0 or split > EXCEL_CELL_LIMIT:
            split = EXCEL_CELL_LIMIT
        ws.cell(row=i, column=2, value=minified[:split])
        ws.cell(row=i, column=3, value=minified[split:])
    ws.cell(row=i, column=4, value=key)
    ws.cell(row=i, column=5, value=len(minified))

# Column widths
ws.column_dimensions['A'].width = 50
ws.column_dimensions['B'].width = 100
ws.column_dimensions['C'].width = 60
ws.column_dimensions['D'].width = 22
ws.column_dimensions['E'].width = 16

wb.save('gameplus-icerikler.xlsx')
```

## Çıkış Konumu

Excel'i CWD'ye (genelde `/Users/Erdo/Desktop/Claude Projects/Dispatch/`) `gameplus-icerikler.xlsx` adıyla kaydet.

## Toplu Üretim Pattern'i

1. Tüm kategoriler için Phase 1 (Playwright count verify) önce
2. Phase 2 (DataForSEO research) ya kategori bazlı ya da common research data ile
3. Phase 3-5 (write + structure) için config-driven Python script
4. Phase 6 (QA) — tüm dosyalar için aynı bash audit
5. Excel rollup

Toplu üretim örneği olarak `/Users/Erdo/Desktop/Claude Projects/Dispatch/` altında `transform_all.py` script'i (eski adıyla `/tmp/transform_all.py`) referans alınabilir; o script 26 kategoriyi tek seferde dönüştürdü.

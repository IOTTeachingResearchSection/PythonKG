from typing import Dict
from pathlib import Path

import fitz  # pip install pymupdf
import sys

if len(sys.argv) < 2:
    print(f'usage: python {sys.argv[0]} pdf_file\n')
    sys.exit(1)

pdf_file = sys.argv[1]
bookmark_file = Path(pdf_file).stem + '.bookmarks.txt'

with fitz.open(pdf_file) as doc, open(bookmark_file, 'w') as outfile:
    toc = doc.get_toc()  # [[lvl, title, page, …], …]
    for level, title, page in toc:
        outfile.write(f"{title}\n")

#!/usr/bin/env python3
from pathlib import Path
import sys

if len(sys.argv) != 3:
    raise SystemExit('usage: patch-release-asset.py <src_html> <dst_html>')

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
html = src.read_text()

if 'id="jl-subtpl-footer-hide"' not in html:
    marker = '</head>'
    if marker not in html:
        raise SystemExit('missing </head> marker')
    inject = (
        '\n<!-- patched by pasarguard-subscription-template-patches -->\n'
        '<style id="jl-subtpl-footer-hide">\n'
        'div[dir="ltr"].relative.w-full.pb-8.pt-6.px-6{display:none!important;}\n'
        '</style>\n'
    )
    html = html.replace(marker, inject + marker, 1)

html = html.replace('Made with ❤️ by \xa0', '')
html = html.replace('Made with ❤️ by  ', '')
html = html.replace('PasarGuard Team', '')

dst.write_text(html)
print(dst)

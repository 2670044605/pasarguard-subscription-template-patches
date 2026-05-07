#!/usr/bin/env python3
from pathlib import Path
import re
import sys

if len(sys.argv) != 3:
    raise SystemExit('usage: patch-release-asset.py <src_html> <dst_html>')

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
html = src.read_text()

# v2.x bundles render a footer component that can include a support-url button
# from response headers. Remove the component itself when the minified shape is
# recognized, and keep the CSS guard below as a defensive fallback.
footer_pattern = (
    r'const EU=\(\)=>\{const\{t:e\}=Pn\(\),\{supportUrl:t\}=xq\(\);'
    r'return N\.jsxs\("div",\{className:"flex flex-col items-center gap-3",children:\[.*?\]\}\)\},TU='
)
html, footer_replacements = re.subn(footer_pattern, 'const EU=()=>null,TU=', html, count=1)
if footer_replacements > 1:
    raise SystemExit(f'unexpected footer replacement count: {footer_replacements}')

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
html = html.replace('title:"应用领域"', 'title:"客户端应用"')

dst.write_text(html)
print(dst)
print(f'footer_component_replacements={footer_replacements}')

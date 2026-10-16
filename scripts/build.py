# usage: python scripts/build.py   -- wraps src/page.html (the artifact fragment) into index.html (standalone page for GitHub Pages)
# @inv: src/page.html is the single source; never hand-edit index.html
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
frag = (root / "src" / "page.html").read_text(encoding="utf-8")
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="description" content="Interactive Big O explorer: every complexity class drawn to scale, plus a searchable catalog of data structures, algorithms, Java calls and loop shapes with their notation.">\n'
        '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif;background:#f7f6f2}img{max-width:100%}[hidden]{display:none!important}</style>\n'
        '</head>\n<body>\n' + frag + '\n</body>\n</html>\n')
(root / "index.html").write_text(html, encoding="utf-8"); print("index.html", len(html), "bytes")

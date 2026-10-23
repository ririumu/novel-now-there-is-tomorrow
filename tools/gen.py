#!/usr/bin/env python3
"""source_data/N.txt -> site/N.html, site/index.html (標準ライブラリのみ)"""
import html, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "source_data"
OUT = ROOT / "site"
BOOK = "Back To The Basic"

PAGE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div id="wrap">
<div id="head">{book}</div>
{body}
<div id="foot">{book}</div>
</div>
</body>
</html>
"""


def e(s):
    return html.escape(s, quote=False)


def split_title(first):
    """【　第一話:知識だ！…　】 -> (第一話, 知識だ！…)"""
    t = re.sub(r"^[【〔\[]\s*|\s*[】〕\]]$", "", first.strip("　 \t"))
    m = re.match(r"(第.+?話)\s*[:：]\s*(.*)", t)
    return (m.group(1), m.group(2).strip()) if m else ("", t)


def chapters():
    files = sorted(SRC.glob("[0-9]*.txt"), key=lambda p: int(p.stem))
    out = []
    for p in files:
        text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
        lines = text.split("\n")
        _, sub = split_title(lines[0])
        body = lines[1:]
        while body and not body[0].strip():
            body.pop(0)
        while body and not body[-1].strip():
            body.pop()
        out.append({"n": int(p.stem), "sub": sub, "body": body,
                    "chars": sum(len(l) for l in body)})
    return out


def nav(n, last):
    prev = f'<a href="{n-1}.html">前へ</a>' if n > 1 else '<span class="off">前へ</span>'
    nxt = f'<a href="{n+1}.html">次へ</a>' if n < last else '<span class="off">次へ</span>'
    return (f'<div class="nav">{prev}<span class="sep">|</span>'
            f'<a href="index.html">目次</a><span class="sep">|</span>{nxt}</div>')


def chapter_page(c, last):
    paras = "\n".join(f"<p>{e(l)}</p>" if l.strip() else "<p><br></p>" for l in c["body"])
    title = f"第{c['n']}話 {c['sub']}"
    body = (f'<div id="crumb"><a href="index.html">トップ</a> &gt; 第{c["n"]}話</div>\n'
            f'<h1>{e(title)}</h1>\n<p class="sub"><a href="index.html">{BOOK}</a></p>\n'
            f'{nav(c["n"], last)}\n<div id="novel">\n{paras}\n</div>\n{nav(c["n"], last)}')
    return PAGE.format(title=e(f"{title} - {BOOK}"), book=BOOK, body=body)


def index_page(cs):
    total = sum(c["chars"] for c in cs)
    rows = "\n".join(
        f'<tr><td class="no">第{c["n"]}話</td><td class="title"><a href="{c["n"]}.html">{e(c["sub"])}</a></td>'
        f'<td class="size">{c["chars"]:,}字</td></tr>' for c in cs)
    synopsis = (SRC / "00_README.md").read_text(encoding="utf-8").strip()
    body = f"""<div id="crumb">トップ</div>
<h1>{BOOK}</h1>
<p class="sub">連載中 ／ 全{len(cs)}話 ／ {total:,}字</p>
<div class="box">
<h2>あらすじ</h2>
{e(synopsis)}
</div>
<table class="toc">
<tr><th colspan="3">目次</th></tr>
{rows}
</table>"""
    return PAGE.format(title=BOOK, book=BOOK, body=body)


def main():
    cs = chapters()
    OUT.mkdir(exist_ok=True)
    for c in cs:
        (OUT / f"{c['n']}.html").write_text(chapter_page(c, len(cs)), encoding="utf-8")
    (OUT / "index.html").write_text(index_page(cs), encoding="utf-8")
    print(f"generated {len(cs)} chapters + index", file=sys.stderr)


if __name__ == "__main__":
    main()

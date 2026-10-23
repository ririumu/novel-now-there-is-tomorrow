# PLAN 1: source_data を static HTML 一式にする

方針: 素の HTML + CSS(JS なし)を `site/` に置く。ビルドツール禁止(ユーザ追記: Makefile と python スクリプトは可)。
古い投稿サイト風 = 白地・細罫線・青リンク・MS Pゴシック系・表組みの目次・「前へ/次へ」ナビ。

- [x] 1. `site/style.css`
- [x] 2. `tools/gen.py` + `Makefile` で `site/index.html` と `site/1..7.html` を生成
- [x] 3. README.md / OVERVIEW.md / REPORT / AUDIT の整備

# PLAN 1: source_data を static HTML 一式にする

方針: ビルドツール不使用。成果物は手で読める素の HTML + CSS 1枚(JS なし)。`site/` に置く。
古いなろう風 = 白地・細罫線・青リンク・MS Pゴシック系・表組みの目次・「前へ/次へ」ナビ。
(なろうのロゴ/名称は使わない)

- [ ] 1. `site/style.css` と `site/index.html`(目次ページ)
- [ ] 2. `site/1.html` 〜 `site/7.html`(本文。source_data/N.txt を 1行=1段落で忠実に変換)
- [ ] 3. README.md / OVERVIEW.md / REPORT / AUDIT の整備

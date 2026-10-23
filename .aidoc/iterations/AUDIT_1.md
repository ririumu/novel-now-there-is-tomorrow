# AUDIT 1
- source_data/ (別リポジトリの gitlink)の 1〜7.txt と 00_README.md を調査。1行=1段落、空行あり、1行目が題名 `【　第一話:…　】` / `〔第二話：…〕`。
- 当初は使い捨て python で変換する想定だったが、ユーザから「Makefile と python は可」との追記があり、`tools/gen.py` + `Makefile` としてリポジトリに残す方針に変更。
- branch feat/style-index: `site/style.css`(白地・細罫線・青リンク・MS Pゴシック・表組み目次)→ main へ --no-ff merge。
- branch feat/generator: gen.py(標準ライブラリのみ、HTML エスケープ、題名の括弧除去、前/次/目次ナビ)。`make site` で 7話+目次を生成 → merge。
- 確認: 全章の `<p>` 数、ナビリンク、目次の字数表示を目視確認。ブラウザでの実表示確認は未実施。
- branch docs/iteration-1: README / OVERVIEW / REPORT。

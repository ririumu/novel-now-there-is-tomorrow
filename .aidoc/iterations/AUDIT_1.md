# AUDIT 1
- source_data/ (別リポジトリの gitlink)の 1〜7.txt と 00_README.md を調査。1行=1段落、空行あり、1行目が題名 `【　第一話:…　】` / `〔第二話：…〕`。
- 当初は使い捨て python で変換する想定だったが、ユーザから「Makefile と python は可」との追記があり、`tools/gen.py` + `Makefile` としてリポジトリに残す方針に変更。
- branch feat/style-index: `site/style.css`(白地・細罫線・青リンク・MS Pゴシック・表組み目次)→ main へ --no-ff merge。
- branch feat/generator: gen.py(標準ライブラリのみ、HTML エスケープ、題名の括弧除去、前/次/目次ナビ)。`make site` で 7話+目次を生成 → merge。
- 確認: 全章の `<p>` 数、ナビリンク、目次の字数表示を目視確認。ブラウザでの実表示確認は未実施。
- branch docs/iteration-1: README / OVERVIEW / REPORT。
- feat/mincho: 本文(#novel)を明朝体スタック(ヒラギノ明朝→游明朝→MS P明朝→Noto Serif JP→serif)に変更、行間2・字間0.04em。目次・UI はゴシックのまま。
- feat/unify-design(デザインレビュー): 目次/本文で h1 の体裁が不一致(ゴシック左寄せ罫線 vs 明朝中央罫線なし)、あらすじ・話タイトルがゴシック、灰色が無彩色で背景の暖色と不統一、色の直書き、を指摘。
  対応: CSS 変数で配色・書体を一元化。読ませる文は明朝、操作部品はゴシックに統一。h1 を両ページで同一(中央・明朝・罫線)にし、本文ページの題名を枠外へ移動(gen.py 修正)。灰色を暖色寄りに統一。480px 以下用の余白調整を追加。
  確認: headless Chrome のスクリーンショットで目次・本文を目視。スマホ幅(480px以下)は headless の最小幅制約で未確認。

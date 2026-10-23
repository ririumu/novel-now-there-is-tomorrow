# OVERVIEW (HEAD)
- `source_data/` : 原稿(別 git リポジトリ。1〜7.txt、題名 00_TITLE.md、あらすじ 00_SYNOPSIS.md、作者のことば 00_README.md)。成果物にしかない文書データは置かない。
- `tools/gen.py` : 原稿 → `site/` を生成する標準ライブラリのみの python スクリプト。
- `Makefile` : `make build`(= `make site`) / `make serve` / `make clean`。
- `site/` : 生成済み static HTML 一式(コミット対象)。`style.css` のみ手書き(Apple 風の静かなデザイン。配色・書体は :root の CSS 変数、ダークモード対応。ヘッダ UI なし)。
- `.aidoc/` : AGENTS.md 規約の計画・監査・報告・入力ログ。

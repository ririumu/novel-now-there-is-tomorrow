# OVERVIEW (HEAD)
- `source_data/` : 原稿(別 git リポジトリ、1〜7.txt + 00_README.md)。
- `tools/gen.py` : 原稿 → `site/` を生成する標準ライブラリのみの python スクリプト。
- `Makefile` : `make site` / `make serve` / `make clean`。
- `site/` : 生成済み static HTML 一式(コミット対象)。`style.css` のみ手書き(配色・書体は :root の CSS 変数で管理)。
- `.aidoc/` : AGENTS.md 規約の計画・監査・報告・入力ログ。

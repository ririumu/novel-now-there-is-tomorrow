# OVERVIEW (HEAD)
- `source_data/` : 原稿(別 git リポジトリ、1〜7.txt + 00_README.md)。
- `tools/gen.py` : 原稿 → `site/` を生成する標準ライブラリのみの python スクリプト。
- `meta/synopsis.txt` : サイト用の一行あらすじ(第一話の前提のみ。ネタバレ禁止。題名はgen.py の BOOK/SUBTITLE)。
- `Makefile` : `make site` / `make serve` / `make clean`。
- `site/` : 生成済み static HTML 一式(コミット対象)。`style.css` のみ手書き(Apple 風の静かなデザイン。配色・書体は :root の CSS 変数、ダークモード対応)。
- `.aidoc/` : AGENTS.md 規約の計画・監査・報告・入力ログ。

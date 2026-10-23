# あの頃にやり直したかったこと

AI がない頃に憧れてみました。(原稿は `source_data/`)

原稿を static HTML(余白と文字組み重視の静かなデザイン)にしたものが `site/` にあります。
`site/index.html` をブラウザで開くだけで読めます。
公開版: https://ririumu.github.io/novel-now-there-is-tomorrow/ (main への push で `site/` を GitHub Pages に配信。`.github/workflows/pages.yml`)

## 誤字脱字の修正手順
```
$EDITOR source_data/3.txt   # 原稿を直す
make build                  # site/*.html を再生成(括弧の対応など体裁崩れは警告が出る)
make serve                  # http://localhost:8000 で確認
```
python3 標準ライブラリのみ。npm 等のビルドツールは使いません。
題名は `00_TITLE.md`、あらすじは `00_SYNOPSIS.md`、作者のことばは `00_README.md` を直せば反映されます。
`source_data/` は別リポジトリなので、原稿の変更はそちらで commit してください。

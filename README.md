# あの頃にやり直したかったこと

AI がない頃に憧れてみました。(原稿は `source_data/`)

原稿を古い小説投稿サイト風の static HTML にしたものが `site/` にあります。
`site/index.html` をブラウザで開くだけで読めます。

## 誤字脱字の修正手順
```
$EDITOR source_data/3.txt   # 原稿を直す
make build                  # site/*.html を再生成(括弧の対応など体裁崩れは警告が出る)
make serve                  # http://localhost:8000 で確認
```
python3 標準ライブラリのみ。npm 等のビルドツールは使いません。
`source_data/` は別リポジトリなので、原稿の変更はそちらで commit してください。

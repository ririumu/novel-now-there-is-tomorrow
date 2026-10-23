# AIなき春に、法を問う (Back To The Basic)

AI がない頃に憧れてみました。(原稿は `source_data/`)

原稿を古い小説投稿サイト風の static HTML にしたものが `site/` にあります。
`site/index.html` をブラウザで開くだけで読めます。

## 再生成
```
make site    # source_data/*.txt -> site/*.html (python3 標準ライブラリのみ)
make serve   # http://localhost:8000
```
npm 等のビルドツールは使いません。

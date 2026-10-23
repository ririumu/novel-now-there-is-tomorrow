# REPORT 1
依頼: source_data の小説を、古い「小説投稿サイト」風デザインの static HTML 一式にする。ビルドツール禁止(後に Makefile と python は許可)。

## 成果
- `site/index.html` 目次(あらすじ・話数・字数)、`site/1.html`〜`7.html` 本文、`site/style.css`。JS・外部読込なし。
- `make site` で再生成。`make serve` で http://localhost:8000 。
- 本文は元テキストを 1行=1`<p>`、空行=`<p><br></p>` で忠実に変換(改稿なし)。

## 注意
- 既存サイトのロゴ・名称は使用せず、雰囲気(配色・罫線・表組み・ナビ)のみ。
- ブラウザでの実機表示確認は未実施。

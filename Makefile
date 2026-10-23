# ビルドツールは使わない。標準ライブラリのみの python3 で source_data から site/ を再生成する。
.PHONY: site serve clean
site:
	python3 -I tools/gen.py

serve: site
	python3 -m http.server 8000 --directory site

clean:
	rm -f site/index.html $(wildcard site/[0-9]*.html)

include ./rvx_init.mh

TEX2HTML_DIR=${CURDIR}/tex2html
MANUAL_LIST=skills-for rvx-web rvx-repository-manual-en rvx-installation-manual-en rvx-cli-manual-en rvx-sw-manual-en rvx-tutorials

include ./tex2html.mh

install:
	${PYTHON3_CMD} -m pip install beautifulsoup4 lxml pypandoc
	@echo ^> Install pacdoc from https://pandoc.org
	@echo ^> Download pandoc-crossref from "https://github.com/lierdakil/pandoc-crossref"
	@echo ^> Move "pandoc-crossref.exe" to "C:\Program Files\Pandoc"

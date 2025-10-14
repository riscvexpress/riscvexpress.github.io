include ./rvx_init.mh

TEX2HTML_DIR=${CURDIR}/tex2html
MANUAL_LIST=skills-for rvx-web rvx-repository-manual-en rvx-installation-manual-en rvx-cli-manual-en rvx-sw-manual-en rvx-fpga-manual-en rvx-tutorials rvx-feature-manual-en

include ./tex2html.mh

install:
	${PYTHON3_CMD} -m pip install beautifulsoup4 lxml pypandoc
	@echo ^> Install pacdoc from https://pandoc.org
	@echo ^> Download pandoc-crossref from "https://github.com/lierdakil/pandoc-crossref"
	@echo ^> Move "pandoc-crossref.exe" to "C:\Program Files\Pandoc"

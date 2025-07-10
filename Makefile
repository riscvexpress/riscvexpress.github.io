include ./rvx_init.mh

MANUAL_LIST=skills-for rvx-web rvx-repository-manual-en rvx-installation-manual-en rvx-cli-manual-en rvx-sw-manual-en rvx-tutorials

clean:
	-del *.zip
	-rmdir ${MANUAL_LIST} /s /q

all: ${MANUAL_LIST}

${MANUAL_LIST}:
	@${PYTHON3_CMD} unzip_tex.py -i ${CURDIR}/$@.zip
	@${PYTHON3_CMD} -c "import shutil, os; d='${CURDIR}/$@'; f='${CURDIR}/rvx-dual-publish-l0.tex'; t=os.path.join(d, 'rvx-dual-publish-l0.tex'); \
os.path.isdir(d) and os.path.exists(t) and os.remove(t); os.path.isdir(d) and shutil.copyfile(f, t)"
	@${PYTHON3_CMD} -c "import shutil, os; d='${CURDIR}/$@'; f='${CURDIR}/rvx-dual-publish-l1.tex'; t=os.path.join(d, 'rvx-dual-publish-l1.tex'); \
os.path.isdir(d) and os.path.exists(t) and os.remove(t); os.path.isdir(d) and shutil.copyfile(f, t)"
	@${PYTHON3_CMD} merge_tex.py -i "${CURDIR}/$@/$@*.tex" -o ${CURDIR}/$@ -p ${CURDIR}/$@
	@${PYTHON3_CMD} rvx_docs.py -cmd latex2html -i ${CURDIR}/$@ -o ${CURDIR} -r ${CURDIR}

install:
	${PIP3_CMD} install --upgrade pip
	${PIP3_CMD} install pypandoc
	@echo "You need to install pandoc separately"

.PHONY: ${MANUAL_LIST}

include ./rvx_init.mh

MANUAL_LIST=skills-for rvx_integration_manual_en rvx_installation_manual_en rvx_cli_manual_en

all: ${MANUAL_LIST}

${MANUAL_LIST}:
	@${PYTHON3_CMD} unzip_tex.py -i ${CURDIR}/$@.zip
	@${PYTHON3_CMD} -c "import shutil, os; d='${CURDIR}/$@'; f='${CURDIR}/rvx_dual_publish_l0.tex'; t=os.path.join(d, 'rvx_dual_publish_l0.tex'); \
os.path.isdir(d) and os.path.exists(t) and os.remove(t); os.path.isdir(d) and shutil.copyfile(f, t)"
	@${PYTHON3_CMD} -c "import shutil, os; d='${CURDIR}/$@'; f='${CURDIR}/rvx_dual_publish_l1.tex'; t=os.path.join(d, 'rvx_dual_publish_l1.tex'); \
os.path.isdir(d) and os.path.exists(t) and os.remove(t); os.path.isdir(d) and shutil.copyfile(f, t)"
	@${PYTHON3_CMD} merge_tex.py -i "${CURDIR}/$@/$@*.tex" -o ${CURDIR}/$@ -p ${CURDIR}/$@
	@${PYTHON3_CMD} rvx_docs.py -cmd latex2html -i ${CURDIR}/$@ -o ${CURDIR} -r ${CURDIR}

install:
	${PIP3_CMD} install --upgrade pip
	${PIP3_CMD} install pypandoc
	@echo "You need to install pandoc separately"

.PHONY: ${MANUAL_LIST}

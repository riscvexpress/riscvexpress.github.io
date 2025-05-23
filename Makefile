include ./rvx_init.mh

MANUAL_LIST=skills-for rvx_install_manual_en rvx_cli_manual_en

all: ${MANUAL_LIST}

${MANUAL_LIST}:
	@${PYTHON3_CMD} rvx_docs.py -cmd latex2html -i ${CURDIR}/$@ -o ${CURDIR} -r ${CURDIR}

install:
	${PIP3_CMD} install --upgrade pip
	${PIP3_CMD} install pypandoc
	@echo "You need to install pandoc separately"

.PHONY: ${MANUAL_LIST}

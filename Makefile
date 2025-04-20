MANUAL_LIST=skills-for-linux rvx_install_manual_en rvx_install_manual_ko

all: ${MANUAL_LIST}

${MANUAL_LIST}:
	@python3 rvx_docs.py -cmd latex2html -i ${CURDIR}/$@ -o ${CURDIR} -r ${CURDIR}

.PHONY: ${MANUAL_LIST}
################################################################################
# GLOBAL VARIABLES
#
# This section lays out some global and high-level commands for the Makefile;
# you can edit them if you like
################################################################################

# ----- How to run the commands ------
PY_INTERP = python
TEX_INTERP = latexmk -cd -e -f -pdf -interaction=nonstopmode

################################################################################
# TEX
#
# Convert yml to latex
################################################################################

tex/talks.tex	:	src/talks.py data/talks.yml src/common.py
	$(PY_INTERP) $<
tex/workshops.tex	:	src/workshops.py data/workshops.yml src/common.py
	$(PY_INTERP) $<
tex/awards.tex	:	src/awards.py data/awards.yml src/common.py
	$(PY_INTERP) $<
tex/teaching.tex	:	src/teaching.py data/teaching.yml src/common.py
	$(PY_INTERP) $<
tex/research.tex	:	src/research.py data/research.yml src/common.py
	$(PY_INTERP) $<
tex/education.tex	:	src/education.py data/education.yml src/common.py
	$(PY_INTERP) $<
tex/conferences.tex	:	src/conferences.py data/conferences.yml src/common.py
	$(PY_INTERP) $<

## make all the latex files from the yml data
tex: tex/talks.tex tex/workshops.tex tex/awards.tex tex/teaching.tex tex/research.tex tex/education.tex tex/conferences.tex

################################################################################
# PDF
#
# build the latex PDF
################################################################################

CV_Doss-Gollin_James.pdf	:	CV_Doss-Gollin_James.tex tex/talks.tex tex/awards.tex
	$(TEX_INTERP) $<

docs/CV_Doss-Gollin_James.pdf	:	CV_Doss-Gollin_James.pdf
	cp $< $@

pdf: tex docs/CV_Doss-Gollin_James.pdf

################################################################################
# Self-Documenting Help Commands
#
# This section contains codes to build automatic help in the makefile
# Copied nearly verbatim from cookiecutter-data-science, in turn taken from
# <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
################################################################################

.DEFAULT_GOAL := help

# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')

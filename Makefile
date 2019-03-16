# Makefile

.PHONY: all

all: docs/CV_Doss-Gollin_James.pdf


tex/experience.tex	:	src/experience.py data/experience.csv
	python $<

CV_Doss-Gollin_James.pdf : CV_Doss-Gollin_James.tex tex/*.tex library.bib CV_Doss-Gollin_James.tex
	latexmk -pdf -xelatex $<

docs/CV_Doss-Gollin_James.pdf : CV_Doss-Gollin_James.pdf
	cp CV_Doss-Gollin_James.pdf docs/CV_Doss-Gollin_James.pdf


$(build_dir):
	mkdir -p $@
pdflatex main
biber main --output-safechars
pdflatex main
pdflatex main
rm main.bbl main.log main.run.xml main.bcf main.out main.aux main.blg
mv main.pdf CV_Doss-Gollin_James.pdf

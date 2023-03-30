pdf: abstract.tex  attack-vectors.tex  attack.tex  conclusion.tex  impact.tex  main.tex  motivation.tex main.bib
	latexmk -f -interaction=nonstopmode -outdir=out/ -pdf main.tex
	cp out/main.pdf .

clean:
	rm -r out/

.PHONY: pdf clean



%.html : %.md
	pandoc -s --mathjax -t slidy $< -o $@

%.pdf : %.md
	pandoc -s --slide-level=2 --mathjax -t beamer $< -o $@


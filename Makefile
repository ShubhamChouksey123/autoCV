PERSON ?= shubham-chouksey
NAME ?= cv
BASE := people/$(PERSON)/$(NAME)

all:
	latexmk -pdf -cd $(BASE).tex

clean:
	rm -f $(BASE).aux $(BASE).bbl $(BASE).bcf $(BASE).fdb_latexmk $(BASE).fls $(BASE).log $(BASE).out $(BASE).run.xml $(BASE).blg $(BASE).toc people/$(PERSON)/*\~

distclean: clean
	rm -f $(BASE).pdf

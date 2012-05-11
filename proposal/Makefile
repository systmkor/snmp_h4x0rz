#
# Team: Ramrod 
#

PROPOSAL_FILE = proposal.pdf
LATEX_FILES = proposal.tex
DVI_OUT = proposal.dvi

all: pdf clean_most

pdf:
	pdflatex $(LATEX_FILES)

clean_all: clean_most
	@rm -f *.pdf

clean_most: clean_extras clean_useless
	@rm -f *.dvi

clean_extras:
	@rm -f *.aux *.log *.

clean_useless:
	@rm -f *~



pdf:


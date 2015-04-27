AUTHOR=Ignas Vyšniauskas

REVEALJSDIR=reveal.js
REVEALJSREPO=git@github.com:hakimel/reveal.js

CSSDIR=css
THEMECSS=$(CSSDIR)/simple.css

REVEALJSTHEME=NONE


CODE_HIGHLIGHT_STYLE=kate

all: slides.html

%.html: %.md template.html Makefile
	pandoc --template=template.html \
		   -s \
		   -S \
		   -t revealjs \
		   --highlight-style $(CODE_HIGHLIGHT_STYLE) \
		   -V theme="$(REVEALJSTHEME)" \
		   -c $(THEMECSS) \
		   -M author="$(AUTHOR)" \
		   -T "Palaipsninis tipavimas Pitone: Type Hints ir mypy - PyConLT 2015 - $(AUTHOR)" \
		    $< -o $@

template.html: $(THEMECSS) | $(REVEALJSDIR)

$(REVEALJSDIR):
	git clone $(REVEALJSREPO) $(REVEALJSDIR)

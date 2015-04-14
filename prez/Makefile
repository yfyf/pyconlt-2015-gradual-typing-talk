AUTHOR=Ignas Vyšniauskas
REVEALJSDIR=reveal.js
REVEALJSREPO=git@github.com:hakimel/reveal.js
REVEALJSTHEME=serif

all: slides.html

%.html: %.md template.html Makefile
	pandoc --template=template.html \
		   -s \
		   -S \
		   -t revealjs \
		   -V theme="$(REVEALJSTHEME)" \
		   -M author="$(AUTHOR)" \
		   -T "Palaipsninis tipavimas Pitone: Type Hints ir mypy - PyConLT 2015 - $(AUTHOR)" \
		    $< -o $@

template.html: | $(REVEALJSDIR)

$(REVEALJSDIR):
	git clone $(REVEALJSREPO) $(REVEALJSDIR)

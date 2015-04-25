Grudually typing Python with gradual types
==========================================

* mypy
* gradual typing
* optional typing in PLs
    + Erlang -- 2007?
    + PHP --- 2014?
    + JS --- 2010?
    + Python .... 2015?
* Success typing

* "ValueClass" / "ValueObject" or whatever it is
  called for more safety

type Counter = Int


Resources
---------

* PEP 483 (Theory of gradual typing):
    https://www.python.org/dev/peps/pep-0483/
* PEP 484 (Type Hints):
    https://www.python.org/dev/peps/pep-0484/
* PEP 484 discussion:
    https://groups.google.com/forum/#!topic/python-ideas/Aa_7lf4jZ7w[1-25]
* GH repo for prototype `typing` module:
    https://github.com/ambv/typehinting
* mypy web and repo:
    https://github.com/JukkaL/mypy
    http://mypy-lang.org/
* mypy wiki:
    http://www.mypy-lang.org/wiki/
* mypy type checker info:
    http://www.mypy-lang.org/wiki/TypeChecker
* Jukka Lethosalo:
    http://www.cl.cam.ac.uk/~jal82/
* mypy generics:
    http://mypy.readthedocs.org/en/latest/generics.html
* What is gradual typing:
    http://wphomes.soic.indiana.edu/jsiek/what-is-gradual-typing/
* Gradual typing bibliography:
    https://github.com/samth/gradual-typing-bib
* Wadler on gradual typing:
    http://homepages.inf.ed.ac.uk/wadler/topics/recent.html
* Gradual evolution:
    http://cacm.acm.org/magazines/2014/10/178775-gradual-evolution/fulltext
    [resources/.pdf]
* Thesis on typing Python:
    http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.90.3231
* "Why Python is slow"
    https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/
* Python internals:
    http://blog.christianperone.com/?p=2171
* Google pytype:
    https://github.com/google/pytype/
* typeannotations:
    https://github.com/ceronman/typeannotations
* stubgen:
    https://github.com/ashleyh/mypy-stubgen
* mypy-stubgen:
    https://github.com/JukkaL/mypy/blob/master/mypy/stubgen.py
* types SIG:
    https://www.python.org/community/sigs/retired/types-sig/
* GvR @ PyCon2015
* Bob @ EuroPython 2014



Presentation ideas
------------------

Use the Haskell-hieroglyphs example to say that well-typing implies you don't even need to look at the code / understand the language to understand what's going on

* Static typing reminds many people of C

    "It is now the 21st century. Computers can drive your cars and bla bla....
     but it can't tell me that this is will always go bad? You gotta be kidding me."

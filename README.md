# tarski-2.0
Old-style computational semantics at the time of Python 3.6

## Overview
This repo has been developed together with the [Medium post](https://towardsdatascience.com/the-meaning-of-life-and-other-nlp-stories-4cbe791ce62a) `The meaning of "life" and other NLP stories`:
it contains classes and data structures to parse formulas in first-order logic and check their truth in a user supplied model. 

The code is commended and written striving for clarity, and mostly for pedagogical purposes (please see the relevant post for more details): 
the idea is to provide a simple-to-follow working project for i) people familiar with model theory that would like to see
it at work in a modern programming language, ii) people familiar with Python, programming and possibly NLP that would like to see
a fully spelled-out model in formal semantics.

The code has been written and tested in Python 3.6.

## Run a sample program 
To run the program, make sure to install the prerequisite dependencies first (we used [lark](https://github.com/lark-parser/lark) to 
quickly build an FOL parser). Then you can run:

```python fol_main.py```

specifying in the `main` which formula and which model you would like to use. Please see the grammar specs in `fol_grammar.py` to get 
a sense of the symbols supported by the implementation. 

The `notebook` folder contains a sketch for a pandas-based semantics (see the blog post for details).


## Tests
Tests built with [pytest](https://docs.pytest.org/). Use

```pytest test_fol_semantics.py```

to run some basic tests (or something like `VIRTUAL_ENV/python -m pytest test_fol_semantics.py` from a virtualenv).

## References
Satisfaction in a model with partial assignments follows closely the exposition of [Language, Proof, Logic](https://www.amazon.com/Language-Proof-Logic-David-Barker-Plummer/dp/1575866323)
(by David Barker-Plummer, Jon Barwise and John Etchemendy), which is also an heavily recommended book to learn first-order logic. A good book on
computational semantics is [Representation and Inference for Natural Language](https://www.press.uchicago.edu/ucp/books/book/distributed/R/bo3685980.html) 
(by Johan Bos and Patrick Blackburn), which contains a detailed discussion on how to build a "model checker" in Prolog
(interestingly, the authors lament that faithful implementations of "vanilla" first-order checkers are very hard to come by ;-)).

Please see the blog post for more references. 

## License
All the code in this repo is provided "AS IS" and it is freely available under the [Apache License Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
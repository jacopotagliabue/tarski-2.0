"""

Simple script showing how to instantiate the grammar and semantics class and evaluate a formula within a
first-order model. This sample script is provided as part of the overall project/tutorial on compositional
semantics: please see README in the repo for further details and additional resources.

"""

from datetime import datetime
from fol_grammar import FolGrammar
from fol_semantics import FolSemantics
from fol_models import FOL_TEST_WORLD

# get service classes for the evaluation
grammar = FolGrammar()
semantics = FolSemantics(grammar)

# program variables
FOL_EXPRESSION = 'Pa'  # change here for a new formula
FOL_MODEL = FOL_TEST_WORLD  # change here to use a different model for the evaluation


def check_formula_in_model(expression, model):
    result = semantics.check_formula_satisfaction_in_model(expression, model)
    print("Formula {} satisfied in the model {}".format(expression, result))

    return result


def main():
    print("Starting evaluation at {}".format(datetime.utcnow()))
    check_formula_in_model(FOL_EXPRESSION, FOL_MODEL)
    print("All done at {}, see you, space cowboys".format(datetime.utcnow()))


if __name__ == "__main__":
    main()

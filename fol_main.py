"""

Simple script showing how to instantiate the grammar and semantics class and evaluate a formula within a
first-order model. This sample script is provided as part of the overall project/tutorial on compositional
semantics: please see README in the repo for further details and additional resources.

"""

from datetime import datetime
from fol_grammar import FolGrammar
from fol_semantics import FolSemantics
from fol_models import FOL_MEDIUM_WORLD

# get service classes for the evaluation
grammar = FolGrammar()
semantics = FolSemantics(grammar)

# program variables
FOL_EXPRESSIONS = [
    'Ij',   # in the Medium post example, "Jacopo is Italian"
    'Qj',  # in the Medium post example, "Jacopo is Canadian"
    '(Ij&Pm)',  # in the Medium post example, "Jacopo is Italian and Mattia is American"
    '-Ij',   # in the Medium post example, "Jacopo is not Italian"
    '(Ij&Qr)',  # in the Medium post example, "Jacopo is Italian and Ryan is Canadian"
    '$x(Px)'  # in the Medium post example, "Somebody is American"
]  # change here for new formulas
FOL_MODEL = FOL_MEDIUM_WORLD  # change here to use a different model for the evaluation


def check_formula_in_model(expression, model):
    result = semantics.check_formula_satisfaction_in_model(expression, model)
    if result:
        print("Formula '{}' satisfied in the model :-)".format(expression))
    else:
        print("Formula '{}' is NOT satisfied in the model :-(".format(expression))

    return result


def main():
    print("Starting evaluation at {}\n".format(datetime.utcnow()))
    for ex in FOL_EXPRESSIONS:
        check_formula_in_model(ex, FOL_MODEL)
    print("\nAll done at {}, see you, space cowboys".format(datetime.utcnow()))


if __name__ == "__main__":
    main()

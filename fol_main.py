from datetime import datetime
from fol_grammar import FolGrammar
from fol_semantics import FolSemantics
from fol_models import FOL_TEST_WORLD

grammar = FolGrammar()
semantics = FolSemantics(grammar)


def main():
    print(semantics.check_formula_satisfaction_in_model("Pa", FOL_TEST_WORLD))
    print("All done at {}, see you, space cowboys".format(datetime.utcnow()))


if __name__ == "__main__":
    main()

from random import choice


class FolSemantics:

    def __init__(self, grammar):
        self.grammar = grammar
        return

    def create_appropriate_assignment(self, domain, free_variables):
        return {free_v: choice(domain) for free_v in free_variables}

    def create_modified_assignment(self, original_assignment, modification):
        new_assignment = original_assignment.copy()
        for var, denotation in modification.items():
            new_assignment[var] = denotation

        return new_assignment

    def check_atomic_formula(self, model, assignment, predicate, args):
        """

        :param model: a dictionary containing constants and extensions for predicates
        :param assignment: mapping variables->domain
        :param predicate: predicate in the formula
        :param args: list of args, len(args) should be == arity of the predicate. Args can be variables or constants
        :return:
        """
        # get args denotation through assignment if variable, through model if constant
        current_denotation = [assignment[v] if self.grammar.is_variable(v) else model['constants'][v] for v in args]
        # check if denotation is in the predicate extension
        return current_denotation in model['extensions'].get(str(predicate), [])

    def check_formula_satisfaction_by_assignment(self, formula, model, assignment):
        """

        :param formula: a lark (sub) tree
        :param model: a dictionary containing constants and extensions for predicates
        :param assignment: mapping variables->domain
        :return:
        """
        # it's an atom
        if formula.data in ['unary', 'binary']:
            # get arguments for the predicate as an array to match the extensions in the model specs
            args = formula.children[1:]
            return self.check_atomic_formula(model, assignment, formula.children[0], args)
        # it's an AND
        elif formula.data == 'and':
            return self.check_formula_satisfaction_by_assignment(formula.children[0], model,assignment) \
                   and self.check_formula_satisfaction_by_assignment(formula.children[1], model, assignment)
        # it's an OR
        elif formula.data == 'or':
            return self.check_formula_satisfaction_by_assignment(formula.children[0], model, assignment) \
                   or self.check_formula_satisfaction_by_assignment(formula.children[1], model, assignment)
        # it's a negation
        elif formula.data == 'neg':
            return not (self.check_formula_satisfaction_by_assignment(formula.children[0], model, assignment))
        # it's an ex quantifier
        elif formula.data == 'q_ex':
            # first child is variable bounded
            bounded_variable = formula.children[0]
            return any([self.check_formula_satisfaction_by_assignment(formula.children[1],
                                                                      model,
                                                                      self.create_modified_assignment(
                                                                          assignment,
                                                                          {bounded_variable: d}))
                        for d in model['domain']
                        ])
        # it's a universal quantifier
        elif formula.data == 'q_un':
            # first child is variable bounded
            bounded_variable = formula.children[0]
            return all([self.check_formula_satisfaction_by_assignment(formula.children[1],
                                                                      model,
                                                                      self.create_modified_assignment(
                                                                          assignment,
                                                                          {bounded_variable: d}))
                        for d in model['domain']
                        ])
        else:
            raise Exception("Operation not defined!")

    def check_formula_satisfaction_in_model(self, expression, model, verbose=False):
        # get the first children as in the Lark grammar the first node is "start"
        formula = self.grammar.parse_expression_with_grammar(expression).children[0]
        free_vars = self.grammar.get_free_variables_from_formula_recursively(formula, [], [])
        assignment = self.create_appropriate_assignment(model['domain'], free_vars)
        if verbose:
            print(formula.pretty(), free_vars, assignment)

        return self.check_formula_satisfaction_by_assignment(formula, model, assignment)

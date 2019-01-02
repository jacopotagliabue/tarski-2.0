from lark import Lark


class FolGrammar:

    FOL_NAMES = ['a', 'b', 'c', 'd', 'e', 'j', 'm', 'r']
    FOL_VARIABLES = ['x', 'y', 'w', 'z']
    FOL_UNARY = ['I', 'P', 'Q', 'R', 'S', 'T', 'U']
    FOL_BINARY = ['A', 'B', 'C', 'D', 'E', 'F']

    LARK_FOL_GRAMMAR_SCHEMA = '''
        start: formula
          
        formula: UNARY (VARIABLE|NAME)     -> unary
            | BINARY (VARIABLE|NAME) (VARIABLE|NAME) -> binary
            | "(" formula "&" formula ")"  -> and
            | "(" formula "^" formula ")"  -> or
            | "-" formula                  -> neg
            | "$" VARIABLE "(" formula ")" -> q_ex
            | "@" VARIABLE "(" formula ")" -> q_un
         
        UNARY: ({})   
        BINARY: ({})
        VARIABLE: ({})
        NAME: ({})
        WHITESPACE: (" " | "\\n")+
        %ignore WHITESPACE
        '''

    def __init__(self):
        """
        Fill the general FOL schema with the actual names, variables, predicates available
        """
        names = '|'.join(['"{}"'.format(n) for n in self.FOL_NAMES])
        variables = '|'.join(['"{}"'.format(v) for v in self.FOL_VARIABLES])
        unary = '|'.join(['"{}"'.format(u) for u in self.FOL_UNARY])
        binary = '|'.join(['"{}"'.format(b) for b in self.FOL_BINARY])
        self.LARK_FOL_GRAMMAR = self.LARK_FOL_GRAMMAR_SCHEMA.format(unary, binary, variables, names)
        # load parser
        self.fol_parser = Lark(self.LARK_FOL_GRAMMAR)

        return

    def parse_expression_with_grammar(self, expression):
        """
        Parse a given expression (a string) to a parse tree according to the grammar, returning None
        if it fails to do so

        :return: Lark parse tree or None if expression cannot be parsed
        """
        try:
            return self.fol_parser.parse(expression)
        except Exception as ex:
            print(ex)
            print('Expression "{}" cannot be parsed'.format(expression))

        return None

    def get_free_variables_from_formula_recursively(self, formula, free_variables, bound_variables):
        """
        Recursively traverse the formula tree and retrieve variables which are free, i.e. variables
        not in the scope of a quantifier.

        :param formula: parsed tree from Lark (possibly sub-tree)
        :param free_variables: list of free variables encountered in parsing
        :param bound_variables: list of bound variables encountered in parsing

        :return: list of all variables (unique values only) that are free in the formula
        """
        # if it is a quantifier node, mark the variable as bound and go on
        if formula.data in ['q_ex', 'q_un']:
            # first child is variable bounded
            bound_variables.append(formula.children[0])
            self.get_free_variables_from_formula_recursively(formula.children[1], free_variables, bound_variables)
        # if it is a terminal, check that variables are not bound/already included in the list
        elif formula.data in ['unary', 'binary']:
            args = formula.children[1:]
            for a in args:
                if self.is_variable(a) and a not in bound_variables and a not in free_variables:
                    free_variables.append(str(a))
        # if anything else, just continue the examination in all children path
        else:
            for f in formula.children:
                self.get_free_variables_from_formula_recursively(f, free_variables, bound_variables)

        return free_variables

    """
    Some utility functions below
    """

    def get_lark_grammar(self):
        return self.LARK_FOL_GRAMMAR

    def is_variable(self, x):
        return x in self.FOL_VARIABLES

    def is_name(self, x):
        return x in self.FOL_NAMES



from lark import Lark


class FolGrammar:

    FOL_NAMES = ['a', 'b', 'c', 'd', 'e']
    FOL_VARIABLES = ['x', 'y', 'w', 'z']
    FOL_UNARY = ['P', 'Q', 'R', 'S', 'T', 'U']
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

    def get_lark_grammar(self):
        return self.LARK_FOL_GRAMMAR

    def is_variable(self, x):
        return x in self.FOL_VARIABLES

    def is_name(self, x):
        return x in self.FOL_NAMES


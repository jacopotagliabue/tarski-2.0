"""
    Example class providing ONLY basic tests!
"""
from fol_grammar import FolGrammar


grammar = FolGrammar()


class TestFolSemantics(object):

    def test_syntactic_parsing(self):
        well_formed_expressions = [
            '(-(Axa & (Rx ^ Rx)) ^ Caz)',
            '($x(Px) & Tx)',
            '$x((Px & Tx))',
            'Pa',
            'Abx'
        ]

        # assert all these are wff
        assert all([grammar.parse_expression_with_grammar(e) for e in well_formed_expressions])

        not_well_formed_expressions = [
            '(-(Axsa & (Rx ^ Rx)) ^ Caz)',
            '($x(Pxa) & Tx)',
            '(Px & Tx) ^ Py',
            'aC'
        ]

        # assert none of these are wff
        assert not(any([grammar.parse_expression_with_grammar(e) for e in not_well_formed_expressions]))

"""
    Example class providing ONLY basic tests!
"""
from fol_grammar import FolGrammar
from fol_semantics import FolSemantics
from fol_models import FOL_TEST_WORLD, FOL_MEDIUM_WORLD


grammar = FolGrammar()
semantics = FolSemantics(grammar)


class TestFolSemantics(object):

    def test_syntactic_parsing(self):
        """
        Test if lark grammar recognizes wff
        """
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

    def test_appropriate_assignments(self):
        """
        Test if service generate assignment which are appropriate for the free variables
        """
        free_variables = [
            ['x'],
            ['z'],
            ['x', 'y'],
            ['x', 'y', 'z'],
            []
        ]

        # assert all assignments are appropriate length
        domain = FOL_TEST_WORLD['domain']
        assert all([len(semantics.create_appropriate_assignment(domain, f).keys()) == len(f) for f in free_variables])

    def test_modified_assignments(self):
        """
        Test a modified assignment g of f is equals to f in all respect except for the variable of interest
        """
        domain = FOL_TEST_WORLD['domain']
        free_variables = [
            (['x'], {'y': 1}),
            (['z'], {'z': 2}),
            (['x', 'y'], {'y': 4}),
            ([], {'z': 3}),
            (['x', 'y', 'z'], {'y': 2, 'x': 4})
        ]
        for fv in free_variables:
            original_assignment = semantics.create_appropriate_assignment(domain, fv[0])
            modified_assignment = semantics.create_modified_assignment(original_assignment, fv[1])
            # assert modified assignment has new values
            for v, d in fv[1].items():
                assert modified_assignment[v] == d
            # assert modified assignment agrees with old on other vars
            for v, d in modified_assignment.items():
                if v not in fv[1]:
                    assert original_assignment[v] == d

    def test_free_variables(self):
        """
        Test if service can recognize which variables are free in a formula
        """
        free_variables_formulas = [
            ('Pa', []),
            ('Px', ['x']),
            ('Aby', ['y']),
            ('@x(Px)', []),
            ('@x((Px&Ry))', ['y']),
            ('@x((Px&Rx))', []),
            ('(Ayz^(Px&Rx))', ['y', 'z', 'x'])
        ]

        # assert all expected free variables are recovered
        for ff in free_variables_formulas:
            formula = grammar.parse_expression_with_grammar(ff[0]).children[0]
            free_vars = grammar.get_free_variables_from_formula_recursively(formula, [],  [])
            # make sure order is not relevant in comparison
            assert sorted(free_vars) == sorted(ff[1])

    def test_atomic_satisfaction(self):
        """
        Test satisfaction of atomic formulas with test world
        """
        atomic_formulas = [
            ({
                 'model': FOL_TEST_WORLD,
                 'assignment': {},
                 'predicate': 'P',
                 'args': ['a']
             }, True),
        ]

        # assert all atomic formulas are (not) satisfied as expected
        assert all([semantics.check_atomic_formula(**a[0]) == a[1] for a in atomic_formulas])

    def test_medium_example(self):
        """
        Test all examples from the Medium post - see README
        """
        medium_examples = [
            ('Ij', True),  # Jacopo IsItalian
            ('Qj', False),  # Jacopo IsCanadian
            ('(Ij&Pm)', False),  # Jacopo IsItalian and Mattia IsAmerican
            ('-Ij', False),  # not Jacopo IsItalian

        ]

        # assert all sample formulas are (not) satisfied as expected
        assert all([semantics.check_formula_satisfaction_in_model(a[0], FOL_MEDIUM_WORLD) == a[1]
                    for a in medium_examples])

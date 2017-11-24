import six
from unittest import TestCase
from greedy_solution import greedy_capacity_finder


class SolutionTestCase(TestCase):

    def test_against_given_conditions_1(self):

        choices = [2, 3, 5]
        test_tuples = (
            # target, expected
            (6,       [3, 3],),
            (9,       [5, 2, 2],),
            (11,      [5, 3, 3],),
        )

        for target, expected in test_tuples:
            actual = greedy_capacity_finder(target, choices)
            six.assertCountEqual(self, expected, actual)

    def test_against_given_conditions_2(self):

        choices = [4, 2]
        test_tuples = (
            # target, expected
            (5,       [4, 2],),
            (8,       [4, 4],),
        )

        for target, expected in test_tuples:
            actual = greedy_capacity_finder(target, choices)
            six.assertCountEqual(self, expected, actual)

    def test_against_other_conditions(self):
        choices = [1, 3, 5, 7, 9]
        test_tuples = (
            # target, expected
            (9,        [9],),
            (10,       [9, 1],),
            (8,        [7, 1],),
            (45,       [9, 9, 9, 9, 9],),
            (46,       [9, 9, 9, 9, 9, 1],),
        )

        for target, expected in test_tuples:
            actual = greedy_capacity_finder(target, choices)
            six.assertCountEqual(self, expected, actual)

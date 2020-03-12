"""
test_US1217
Author: Xinyi Ye
Date: 03/12/2020
"""


from unittest import TestCase
import unittest
from gedcom_app.control.US1217 import parents_not_too_old_us12, no_marriage_to_children_us17
from gedcom_app.tests.build_instance import build_family_list, build_individual_list


class TestUS1217(TestCase):
    """
    test US12: parents_not_too_old
    test US17: no_marriage_to_children
    """
    def test_parents_not_too_old_us12(self):
        family_dict = build_family_list()
        parents_not_too_old_us12(family_dict)
        self.assertEqual([str(error) for error in family_dict['F4'].error_list],
                         ["ERROR: FAMILY: US12: 61: F4: "
                          "father I09 7 Jul 1923 is not less than 80 years old than child I08 7 Jul 2003",
                          "ERROR: FAMILY: US12: 69: F4: "
                          "mother I10 7 Jul 1942 is not less than 60 years old than child I08 7 Jul 2003"])

    def test_no_marriage_to_children_us17(self):
        family_dict = build_family_list()
        no_marriage_to_children_us17(family_dict)
        self.assertEqual([str(error) for error in family_dict['F5'].error_list],
                         ["ERROR: FAMILY: US17: 51: F5: mother I10 married to her child I08"])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
"""
test_US0203
Author: Xinyi Ye
Date: 03/12/2020
"""


from unittest import TestCase
import unittest
from gedcom_app.control.US0203 import birth_b_marriage_us02, birth_b_death_us03
from gedcom_app.tests.build_instance import build_family_list, build_individual_list


path = r"..\..\test.ged"


class TestUS0203(TestCase):
    """
        test US02: birth before marriage
        test US03: birth before death
    """
    def test_birth_b_marriage_us02(self):
        family_dict = build_family_list(path)
        birth_b_marriage_us02(family_dict)
        self.assertEqual([str(error) for error in family_dict['F2'].error_list],
                         ["ERROR: FAMILY: US02: 26: F2:  "
                          "wife I04 birthday 4 May 2022 isn't before married date 5 FEB 1997"])
        self.assertEqual([str(error) for error in family_dict['F3'].error_list],
                         ["ERROR: FAMILY: US02: 26: F3:  "
                          "wife I04 birthday 4 May 2022 isn't before married date 5 JAN 1992"])

    def test_birth_b_death_us03(self):
        indi_dict = build_individual_list(path)
        birth_b_death_us03(indi_dict)
        self.assertEqual([str(error) for error in indi_dict['I01'].error_list],
                         ["ERROR: INDIVIDUAL: US03: 5: I01: "
                          "I01's birthday 5 JUL 1950 isn't before death date 31 DEC 1949"])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

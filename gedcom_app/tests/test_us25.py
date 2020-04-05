"""
US25
Author: Xinyi Ye
Date: 03.31.2020
"""


from unittest import TestCase
import unittest
from gedcom_app.control.US2527 import unique_first_names_in_families_us25
from gedcom_app.tests.build_instance import build_family_list

PATH = r"..\..\test2527.ged"


class TestUS25(TestCase):
    """
        test US25: Unique first names in families
    """

    def test_unique_first_names_in_families_us25(self):
        family_dict = build_family_list(PATH)
        unique_first_names_in_families_us25(family_dict)
        self.assertEqual([str(error) for error in family_dict['125F1'].error_list],
                         ["ANOMALY: FAMILY: US25: 114: 125F1: "
                          "children ['025I03', '025I04', '025I05'] of family 125F1 have the same first name 'GuGu'"])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
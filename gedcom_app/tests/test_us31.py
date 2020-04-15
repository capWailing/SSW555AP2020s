"""
test US31: List living single
Author: Xinyi Ye
Date: 04.10.2020
"""
from unittest import TestCase
import unittest
from gedcom_app.control.US31 import list_living_single_us31
from gedcom_app.control.parser import parse_gedcom
from gedcom_app.control.build_entity import build_individual


PATH = r"..\..\test3132.ged"


class TestUS31(TestCase):
    """
    US31:List living single
    """
    def test_list_living_single_us31(self):
        dict_indi, dict_fam = parse_gedcom(PATH)
        indi_list = build_individual(dict_indi)
        list_result = list_living_single_us31(indi_list)
        self.assertEqual(list_result, ['014I03', '014I04', '014I05', '014I06', '014I07', '014I08', '031I03'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
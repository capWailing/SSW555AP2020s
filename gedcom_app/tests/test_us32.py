"""
test US32: list multiple birth
Author: Xinyi Ye
Date: 04.10.2020
"""
from unittest import TestCase
import unittest
from gedcom_app.control.US32 import list_multiple_birth_us32
from gedcom_app.control.parser import parse_gedcom
from gedcom_app.control.build_entity import build_individual, build_family


PATH = r"..\..\test3132.ged"


class TestUS32(TestCase):
    """
    US32: list multiple birth
    """
    def test_list_multiple_birth_us32(self):
        dict_indi, dict_fam = parse_gedcom(PATH)
        indi_list = build_individual(dict_indi)
        fam_list = build_family(dict_fam, indi_list)
        list_result = list_multiple_birth_us32(fam_list)
        self.assertEqual(list_result,
                         [['014I03', '014I04', '014I05', '014I06', '014I07', '014I08'], ['032I03', '032I05'],
                          ['032I08', '032I09', '032I10']])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
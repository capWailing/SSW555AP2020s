"""
US27
Author: Xinyi Ye
Date: 03.31.2020
"""

from unittest import TestCase
import unittest
from gedcom_app.control.parser import parse_gedcom
from gedcom_app.control.build_entity import build_individual
from gedcom_app.view.output_prettytable import individual_table

PATH = r"..\..\test2527.ged"


class TestUS27(TestCase):
    """
    test US27: Include individual ages
    """
    def test_include_individual_ages_us27(self):
        dict_indi, dict_fam = parse_gedcom(PATH)
        indi_list = build_individual(dict_indi)
        tb = individual_table(indi_list)
        l_age = []
        for row in tb:
            row.border = False
            row.header = False
            l_age.append(row.get_string(fields=["Age"]).strip())

        self.assertEqual(tb.field_names,
                         ['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death', 'Child', 'Spouse', 'Age'])
        self.assertEqual(l_age, ['death age: 0', '69', '51', '-2', '25', '21', 'death age: 25', '16', 'death age: 60',
                                 '77', 'death age: 0', '69', '51', '51', '51', '51', '51', '51', 'death age: 283',
                                 '69', '51', '-2', '25', '21', 'death age: 21', '47', '45', '22', '19', '17'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
import unittest

from gedcom_app.control.US15 import multiple_siblings
from gedcom_app.tests.build_instance import build_family_list


class TestMultipleSiblings(unittest.TestCase):
    def test_multiple_siblings(self):
        path = r"..\..\test15.ged"
        family_dict = build_family_list(path)
        multiple_siblings(family_dict)
        self.assertEqual([str(error) for error in family_dict['115F1'].error_list],
                         ["ERROR: FAMILY: US15: 103: 115F1: More than 15 siblings in one family."])
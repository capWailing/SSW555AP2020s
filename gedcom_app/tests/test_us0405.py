from unittest import TestCase
import unittest
from gedcom_app.control.US0405 import USO4, US05
from gedcom_app.tests.build_instance import build_family_list

path = r"..\..\test(4 5 11 19 23).ged"


class Test(TestCase):

    def test_US04(self):
        family_dict = build_family_list(path)
        USO4(family_dict)
        self.assertEqual([str(error) for error in family_dict['104F1'].error_list],
                         ['Error: FAMILY: US04: 55: 104F1: Divorced 18 May 1888 before married 17 FEB 1966'])

    def test_US05(self):
        family_dict = build_family_list(path)
        US05(family_dict)
        self.assertEqual([str(error) for error in family_dict['104F3'].error_list],
                         ["Error: FAMILY: US05: 70: 104F3: Married 5 JAN 1992 after husband's (004I07) death on 11 DEC 1991"])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

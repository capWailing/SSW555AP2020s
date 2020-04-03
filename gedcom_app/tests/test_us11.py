from unittest import TestCase
import unittest
from gedcom_app.control.US11 import US11
from gedcom_app.tests.build_instance import build_family_list, build_individual_list

path = r"..\..\test040511.ged"


class Test(TestCase):

    def test_US11(self):
        individual_dict = build_individual_list(path)
        family_dict = build_family_list(path)
        US11(individual_dict, family_dict)

        self.assertEqual([str(error) for error in individual_dict['004I04'].error_list],
                         ['Error: INDIVIDUAL: US11: 61: 004I04: bigamy happened on family 104F2 and family 104F3'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
from unittest import TestCase
import unittest
from gedcom_app.control.child_birth import birth_before_marriage
from gedcom_app.tests.build_instance import build_family_list


class TestBirthBeforeMarriage(TestCase):
    def test_birth_before_marriage(self):
        family_dict = build_family_list()
        birth_before_marriage(family_dict)
        self.assertEqual([str(error) for error in family_dict['F1'].error_list],
                         ["ANOMALY: FAMILY: US08: 19: F1: Child I03 born "
                          "1968-06-05 00:00:00 before marriage on 2001-02-17 00:00:00",
                          "ANOMALY: FAMILY: US09: 19: F1: Child I03 born 1968-06-05 "
                          "00:00:00 after daddy's death on 1949-12-31 00:00:00"])
        self.assertEqual([str(error) for error in family_dict['F2'].error_list],
                         ["ANOMALY: FAMILY: US08: 33: F2: Child I05 born 1994-06-05"
                          " 00:00:00 before marriage on 1997-02-05 00:00:00"])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
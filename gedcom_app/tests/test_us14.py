from unittest import TestCase
from gedcom_app.control.child_birth import birth_before_marriage
from gedcom_app.control.us14 import multiple_birth
from gedcom_app.tests.build_instance import build_family_list

path = r"..\..\test14.ged"


class TestBirthBeforeMarriage(TestCase):
    def test_birth_before_marriage(self):
        family_dict = build_family_list(path)
        multiple_birth(family_dict)
        self.assertEqual([str(error) for error in family_dict['F1'].error_list],
                         ["ERROR: FAMILY: US14: 43: F1: More than 5 siblings born at the same day."])

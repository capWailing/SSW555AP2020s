from unittest import TestCase
import unittest
from gedcom_app.control.US1923 import first_cousin_should_not_marry_us19, unique_name_and_birthday_us23
from gedcom_app.tests.build_instance import build_family_list, build_individual_list

path1 = r"..\..\test19.ged"
path2 = r"..\..\test23.ged"


class Test(TestCase):
    def test_first_cousin_should_not_marry_us19(self):
        family_dict = build_family_list(path1)
        first_cousin_should_not_marry_us19(family_dict)
        self.assertEqual([str(error) for error in family_dict['119F5'].error_list],
                         ['Error: FAMILY: US19: 104: 119F5: First cousins marry one another happened in family 119F5'])

    def test_unique_date_and_birthday_us23(self):
        individual_dict = build_individual_list(path2)
        unique_name_and_birthday_us23(individual_dict)
        self.assertEqual([str(error) for error in individual_dict['023I01'].error_list],
                         ['Error: INDIVIDUAL: US23: 3: 023I01: more than one individual with same name '
                          'Qiang /Wang/ and birth date 5 JUL 1950 appear in the GED file'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

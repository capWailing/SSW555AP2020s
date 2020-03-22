from unittest import TestCase
from gedcom_app.control.us0106 import div_before_death,date_before_current
from gedcom_app.tests.build_instance import build_family_list,build_individual_list


class TestUS1018(TestCase):

    def test_div_before_death(self):
        path = r"..\..\test.ged"
        family_dict = build_family_list(path)
        div_before_death(family_dict)

        self.assertEqual([str(error) for error in family_dict['F1'].error_list],
                         ["ERROR: FAMILY: US06: 79: F1: divorce date 1996-05-18 00:00:00 "
                          "after husband's death 1949-12-31 00:00:00"])

    def test_date_before_current(self):
        path = r"..\..\test.ged"
        family_dict = build_family_list(path)
        indi_dict=build_individual_list(path)
        date_before_current(indi_dict,family_dict)

        self.assertEqual([str(error) for error in indi_dict['I04'].error_list],
                         ["ERROR: INDIVIDUAL: US01: 26: I04: birthday date 2022-05-04 00:00:00 before today"])
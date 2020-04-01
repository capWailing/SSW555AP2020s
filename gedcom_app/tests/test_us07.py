from unittest import TestCase

from gedcom_app.control.us07 import less_than_150
from gedcom_app.tests.build_instance import build_individual_list

path = r'..\..\test07.ged'


class TestLessThan150(TestCase):
    def test_less_than_150(self):
        indi_dict = build_individual_list(path)
        less_than_150(indi_dict)
        self.assertEqual([str(error) for error in indi_dict['I1'].error_list],
                         ["ERROR: INDIVIDUAL: US07: 9: I1: "
                          "Jenny /Smith/'s age should be less than 150 years."])
        self.assertEqual([str(error) for error in indi_dict['I2'].error_list],
                         ["ERROR: INDIVIDUAL: US07: 15: I2: "
                          "Michael /Wilson/ should no more than 150 years old."])
        self.assertEqual([str(error) for error in indi_dict['I3'].error_list],
                         [])
        self.assertEqual([str(error) for error in indi_dict['I4'].error_list],
                         [])

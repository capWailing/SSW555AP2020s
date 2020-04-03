from unittest import TestCase
from gedcom_app.control.US2124 import corrent_gender_us21,unique_family
from gedcom_app.tests.build_instance import build_family_list


class TestUS1018(TestCase):

    def test_corrent_gender_us21(self):
        path = r"..\..\test2124.ged"
        family_dict = build_family_list(path)
        corrent_gender_us21(family_dict)

        self.assertEqual([str(error) for error in family_dict['F1211'].error_list],
                         ["ANOMALY: FAMILY: US21: 37: F1211: husband's gender should be female",
                          "ANOMALY: FAMILY: US21: 38: F1211: wife's gender should be male"])

    def test_sibi_not_marry(self):
        path = r"..\..\test2124.ged"
        family_dict = build_family_list(path)
        unique_family(family_dict)

        self.assertEqual([str(error) for error in family_dict['F1242'].error_list],
                         ["ANOMALY: FAMILY: US24: 46: F1242: wife should have same marry date in different family"])
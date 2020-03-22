from unittest import TestCase
from gedcom_app.control.sibi_not_marry import sibi_not_marry
from gedcom_app.control.marr_after_14 import marry_after_14
from gedcom_app.tests.build_instance import build_family_list


class TestUS1018(TestCase):

    def test_marry_after_14(self):
        path = r"C:\Users\wangd\PycharmProjects\SSW555AP2020s\test1.ged"
        family_dict = build_family_list(path)
        marry_after_14(family_dict)

        self.assertEqual([str(error) for error in family_dict['F2'].error_list],
                         ["ANOMALY: FAMILY: US10: 78: F2: Child I04's marry date is 1997-02-05 00:00:00,"
                          "less than 14 years after 1990-05-04 00:00:00 "])

    def test_sibi_not_marry(self):
        path = r"C:\Users\wangd\PycharmProjects\SSW555AP2020s\test1.ged"
        family_dict = build_family_list(path)
        sibi_not_marry(family_dict)

        self.assertEqual([str(error) for error in family_dict['F5'].error_list],
                         ["ANOMALY: FAMILY: US18: 94: F5: Siblings should not marry one another"])
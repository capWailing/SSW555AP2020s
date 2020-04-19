"""
    author: Zituo Yan
    description: test us 26
    date: 19/04/2020
"""
from unittest import TestCase

from gedcom_app.control.US26 import indi_corresponding_in_family, family_corresponding_in_indi
from gedcom_app.tests.build_instance import build_family_list, build_individual_list

PATH = r"..\..\test26.ged"


# "Error: Family: US26: 35: 126I01: Corresponding issue happened."

class TestCorresponding(TestCase):
    def test_corresponding_family(self):
        indi_dict = build_individual_list(PATH)
        fam_dict = build_family_list(PATH)
        indi_corresponding_in_family(indi_dict, fam_dict)
        self.assertEqual([str(error) for error in fam_dict['126I01'].error_list],
                         ['Error: Family: US26: 57: 126I01: Corresponding issue happened. Family '
                          "126I01's children 026I04 has wrong family Id."])
        self.assertEqual([str(error) for error in fam_dict['126I02'].error_list],
                         ["Error: Family: US26: 61: 126I02: Corresponding issue happened. "
                          "Family 126I02's spouse 026I06 has wrong family Id.",
                          "Error: Family: US26: 62: 126I02: Corresponding issue happened. "
                          "Family 126I02's spouse 026I05 has wrong family Id.",
                          "Error: Family: US26: 63: 126I02: Corresponding issue happened. "
                          "Family 126I02's children 026I03 has wrong family Id."])

    def test_corresponding_indi(self):
        indi_dict = build_individual_list(PATH)
        fam_dict = build_family_list(PATH)
        family_corresponding_in_indi(indi_dict, fam_dict)
        self.assertEqual([str(error) for error in indi_dict['026I06'].error_list],
                         ['Error: Individual: US26: 39: 026I06: Corresponding issue happened. 126I03 '
                          'not found in family list.'])
        self.assertEqual([str(error) for error in indi_dict['026I04'].error_list],
                         ['Error: Individual: US26: 26: 026I04: Corresponding issue happened. '
                          'Family 126I02 does not have individual 026I04.'])
        self.assertEqual([str(error) for error in indi_dict['026I07'].error_list],
                         ['Error: Individual: US26: 45: 026I07: Corresponding issue happened. '
                          'Family 126I02 does not have individual 026I07.'])
        self.assertEqual([str(error) for error in indi_dict['026I08'].error_list],
                         ['Error: Individual: US26: 51: 026I08: Corresponding issue happened. '
                          'Family 126I02 does not have individual 026I08.'])

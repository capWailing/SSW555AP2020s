import unittest
from io import StringIO
from unittest.mock import patch

from gedcom_app.tests.build_instance import build_family_list, build_individual_list


class TestUniqueID(unittest.TestCase):
    def test_unique_indi_id(self):
        path = r"..\..\test22.ged"
        indi_dict = build_individual_list(path)
        self.assertEqual([str(error) for error in indi_dict['022I01'].error_list],
                         ["ERROR: INDIVIDUAL: US22: 9: 022I01: Individual ID 022I01 should be unique!"])
        self.assertEqual([str(error) for error in indi_dict['022I02'].error_list],
                         ["ERROR: INDIVIDUAL: US22: 23: 022I02: Individual ID 022I02 should be unique!"])

    def test_unique_fam_id(self):
        path = r"..\..\test22.ged"
        family_dict = build_family_list(path)
        self.assertEqual([str(error) for error in family_dict['122F1'].error_list],
                         ["ERROR: FAMILY: US22: 36: 122F1: Family ID 122F1 should be unique!"])

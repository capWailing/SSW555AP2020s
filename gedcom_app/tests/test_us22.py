import unittest
from io import StringIO
from unittest.mock import patch

from gedcom_app.tests.build_instance import build_family_list, build_individual_list


class TestUniqueID(unittest.TestCase):
    def test_unique_indi_id(self):
        path = r"..\..\test22.ged"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            build_individual_list(path)
            self.assertEqual(fake_out.getvalue(), """ERROR: INDI: US22: 1: 022I01: INDI ID 022I01 should be unique!
ERROR: INDI: US22: 9: 022I01: INDI ID 022I01 should be unique!
ERROR: INDI: US22: 15: 022I02: INDI ID 022I02 should be unique!
ERROR: INDI: US22: 23: 022I02: INDI ID 022I02 should be unique!
""")

    def test_unique_fam_id(self):
        path = r"..\..\test22.ged"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            build_family_list(path)
            self.assertEqual(fake_out.getvalue(), """ERROR: INDI: US22: 1: 022I01: INDI ID 022I01 should be unique!
ERROR: INDI: US22: 9: 022I01: INDI ID 022I01 should be unique!
ERROR: INDI: US22: 15: 022I02: INDI ID 022I02 should be unique!
ERROR: INDI: US22: 23: 022I02: INDI ID 022I02 should be unique!
ERROR: FAM: US22: 29: 122F1: FAM ID 122F1 should be unique!
ERROR: FAM: US22: 36: 122F1: FAM ID 122F1 should be unique!
""")

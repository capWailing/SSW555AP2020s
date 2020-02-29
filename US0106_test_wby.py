import unittest
from unittest.mock import patch
from Project04_xye import parse_GEDCOM
from US0106_wby import US01,US06

class Test(unittest.TestCase):   
    
    def test_US01(self):
        m, n = parse_GEDCOM('test_US0106.ged')
        with patch('builtins.print') as mocked_print:
            US01(m,n)
            mocked_print.assert_called_with("ERROR: INDIVIDUAL: US01: 26:I04: birth date 4 May 2022 before today")
            
    def test_US06(self):
        m, n = parse_GEDCOM('test_US0106.ged')
        with patch('builtins.print') as mocked_print:
            US06(m,n)
            mocked_print.assert_called_with("ERROR: FAMILY: US06: 55: F1:hunsband's death date 31 DEC 1949 before divorce date 18 May 1996")
         



if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

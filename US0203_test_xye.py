import unittest
from unittest.mock import patch
from project04_n_xye import parse_GEDCOM
from US0203_xye import US02, US03

class Test(unittest.TestCase):   
    
    def test_US02(self):
        m, n = parse_GEDCOM('test0203.ged')
        with patch('builtins.print') as mocked_print:
            US02(m, n)
            mocked_print.assert_called_with("Error: FAMILY: US02 birth before marriage：line 5 and 32: I01: 15 JUL 1985 isn't before 29 FEB 1980")
            
    def test_US03(self):
        m, n = parse_GEDCOM('test0203.ged')
        with patch('builtins.print') as mocked_print:
            US03(m)
            mocked_print.assert_called_with("Error: INDIVITUAL: US03 birth before death：line 5 and 9: I01: 15 JUL 1985 isn't before 15 JUL 1984")
         
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
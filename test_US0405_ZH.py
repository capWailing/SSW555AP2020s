import unittest
from unittest.mock import patch
from project04_n_xye import parse_GEDCOM
from US0405_ZH import USO4, US05


class Test(unittest.TestCase):

    def test_US04(self):
        m, n = parse_GEDCOM('test_US0405.ged')
        with patch('builtins.print') as mocked_print:
            USO4(n)
            mocked_print.assert_called_with('Error: FAMILY: US04: 55: F1: Divorced 18 May 1888 before married 17 FEB 1966')

    def test_US05(self):
        m, n = parse_GEDCOM('test_US0405.ged')
        with patch('builtins.print') as mocked_print:
            US05(m, n)
            mocked_print.assert_called_with("Error: FAMILY: US05: 68: F3: Married 5 JAN 1992 after husband's (I07) death on 11 DEC 1991")


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

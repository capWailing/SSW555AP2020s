import unittest
from unittest.mock import patch
from Project04_xye import parse_GEDCOM
from us0809_child_birth import birth_before_marriage


class Test(unittest.TestCase):

    def test_US08(self):
        m, n = parse_GEDCOM('test03.ged')
        with patch('builtins.print') as mocked_print:
            birth_before_marriage(m, n)
            mocked_print.assert_called_with(
                "ANOMALY: FAMILY: US08: 13: @F4@: Child @I2@ born 1970-05-13 00:00:00 before marriage on 1977-11-15 00:00:00")



if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
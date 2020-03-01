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
                "ANOMALY: FAMILY: US08: 20: @F3@: Child @I3@ born 1973-07-10 00:00:00 after divorce on 1970-05-11 00:00:00")



if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
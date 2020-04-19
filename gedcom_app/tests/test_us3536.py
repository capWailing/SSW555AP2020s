"""
Author: Zhiqiang Huang
Date: 04/17/2020
"""
from unittest import TestCase
import unittest
from gedcom_app.control.US3536 import recent_deaths, recent_births
from gedcom_app.tests.build_instance import build_individual_list

Path1 = r"..\..\test35.ged"
Path2 = r"..\..\test36.ged"


class TestUS35(TestCase):
    def test_recent_births_us35(self):
        indi = build_individual_list(Path1)
        list_result = recent_births(indi)
        self.assertEqual(list_result, ['135I01', '135I02'])


class TestUS36(TestCase):
    def test_recent_deaths_us36(self):
        indi = build_individual_list(Path2)
        list_result = recent_deaths(indi)
        self.assertEqual(list_result, ['136I01'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

"""
    author: Zituo Yan
    description: test us 38
    date: 19/04/2020
"""
from unittest import TestCase

from gedcom_app.control.US38 import list_birthday_recent
from gedcom_app.control.build_entity import build_individual
from gedcom_app.control.parser import parse_gedcom

PATH = r"..\..\test38.ged"


class TestUS38(TestCase):
    """
    US31:List living single
    """
    def test_list_living_single_us31(self):
        dict_indi, dict_fam = parse_gedcom(PATH)
        indi_list = build_individual(dict_indi)
        list_result = list_birthday_recent(indi_list)
        self.assertEqual(list_result, ['038I02', '038I05'])

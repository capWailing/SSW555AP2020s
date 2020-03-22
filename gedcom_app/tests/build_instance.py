"""
    author: Zituo Yan
    description: Build instance of family and individual for other tests
    date: 11/03/2020
"""
from gedcom_app.control.build_entity import build_individual, build_family
from gedcom_app.control.parser import parse_gedcom

PATH = r"..\..\test.ged"


def build_individual_list(path):
    return build_individual(parse_gedcom(path)[0])


def build_family_list(path):
    result = parse_gedcom(path)[1]
    return build_family(result, build_individual_list(path))

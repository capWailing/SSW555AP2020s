"""
    author: Zituo Yan
    description: Build instance of family and individual for other tests
    date: 11/03/2020
"""
from gedcom_app.control.build_entity import build_individual, build_family
from gedcom_app.control.parser import parse_gedcom

PATH = r"..\..\test.ged"


def build_individual_list():
    return build_individual(parse_gedcom(PATH)[0])


def build_family_list():
    result = parse_gedcom(PATH)
    return build_family(result[1], build_individual_list())

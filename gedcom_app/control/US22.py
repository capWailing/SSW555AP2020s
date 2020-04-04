"""
    author: Zituo Yan
    description: individual id and family id should be unique
    date: 03/04/2020
"""
from collections import defaultdict


def unique_indi_id(indi):
    id_list = [people["INDI"] for people in indi]
    total = defaultdict(list)
    for item in id_list:
        total[item[0]].append(item[1])
    for key, value in total.items():
        if len(value) > 1:
            for i in value:
                output_not_unique("INDI", key, i)


def unique_fam_id(fam):
    id_list = [family["FAM"] for family in fam]
    total = defaultdict(list)
    for item in id_list:
        total[item[0]].append(item[1])
    for key, value in total.items():
        if len(value) > 1:
            for i in value:
                output_not_unique("FAM", key, i)


def output_not_unique(id_type, id_value, id_location):
    print(f"ERROR: {id_type}: US22: {id_location}: {id_value}: {id_type} ID {id_value} should be unique!")

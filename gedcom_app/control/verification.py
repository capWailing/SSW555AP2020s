"""
    author: Zituo Yan
    description: this starts the verification part
    date: 3/2/2020
"""
from gedcom_app.control.child_birth import birth_before_marriage


def verification(indi_dict, fam_dict):
    birth_before_marriage(fam_dict)

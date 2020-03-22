"""
    author: Zituo Yan
    description: this starts the verification part
    date: 3/2/2020
"""
from gedcom_app.control.child_birth import birth_before_marriage
from gedcom_app.control.us07 import less_than_150
from gedcom_app.control.us14 import multiple_birth


def verification(indi_dict, fam_dict):
    birth_before_marriage(fam_dict)
    less_than_150(indi_dict)
    multiple_birth(fam_dict)

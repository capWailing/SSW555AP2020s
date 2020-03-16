"""
    author: Zituo Yan
    description: this starts the verification part
    date: 3/2/2020
"""
from gedcom_app.control.child_birth import birth_before_marriage
from gedcom_app.control.marr_after_14 import marry_after_14
from gedcom_app.control.sibi_not_marry import sibi_not_marry

def verification(indi_dict, fam_dict):
    birth_before_marriage(fam_dict)
    marry_after_14(fam_dict)
    sibi_not_marry(fam_dict)


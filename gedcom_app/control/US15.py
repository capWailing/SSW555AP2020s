"""
    author: Zituo Yan
    description: US 14 no more than 5 siblings should born at the same time
    date: 03/04/2020
"""
from gedcom_app.errors.gedcom_error import GedcomError


def multiple_siblings(fam):
    for key, family in fam.items():
        if len(family.children) > 15:
            new_error = GedcomError(("ERROR", "FAMILY", "US15", family.children[15].indi_id[1], key),
                                    f"More than 15 siblings in one family.")
            family.error_list = new_error

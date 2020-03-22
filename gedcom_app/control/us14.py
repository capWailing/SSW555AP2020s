"""
    author: Zituo Yan
    description: US 14 no more than 5 siblings should born at the same time
    date: 21/03/2020
"""
from datetime import datetime

from gedcom_app.errors.gedcom_error import GedcomError


def multiple_birth(fam):
    for key, family in fam.items():
        if len(family.children) > 5 and \
                len(set([datetime.strptime(child.birthday[0], "%d %b %Y") for child in family.children])) == 1:
            new_error = GedcomError(("ERROR", "FAMILY", "US14", family.children[4].birthday[1], key),
                                    f"More than 5 siblings born at the same day.")
            family.error_list = new_error

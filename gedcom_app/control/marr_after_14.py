"""
    author: boyu wang
    description: Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
    date: 07/03/2020
"""
from datetime import datetime

from gedcom_app.errors.gedcom_error import GedcomError


def marry_after_14(fam):
    for key, family in fam.items():
        marr_date = datetime.strptime(family.married[0], "%d %b %Y")
        husband_id = family.husband[0]
        wife_id = family.wife[0]
        hus_birth = datetime.strptime(husband_id.birthday[0], "%d %b %Y")
        wife_birth=datetime.strptime(wife_id.birthday[0], "%d %b %Y")

        days1 = marr_date - hus_birth
        days2 = marr_date - wife_birth

        if days1.days <= 14*365.25:
            new_error = GedcomError(("ANOMALY", "FAMILY", "US10", family.married[1], key),
                                    f"Child {husband_id.indi_id[0]}'s marry date is {marr_date},"
                                    f"less than 14 years after {hus_birth} ")
            family.error_list = new_error

        if days2.days <= 14*365.25:
            new_error = GedcomError(("ANOMALY", "FAMILY", "US10", family.married[1], key),
                                    f"Child {wife_id.indi_id[0]}'s marry date is {marr_date},"
                                    f"less than 14 years after {wife_birth} ")
            family.error_list = new_error
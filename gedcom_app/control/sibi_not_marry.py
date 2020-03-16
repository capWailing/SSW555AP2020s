"""
    author: boyu wang
    description: Siblings should not marry one another
    date: 11/03/2020
"""
from collections import defaultdict

from gedcom_app.errors.gedcom_error import GedcomError


def sibi_not_marry(fam):
    fami = {}

    for key, family in fam.items():
        husband = family.husband[0]
        wife = family.wife[0]

        if husband.child != 'N/A' and wife.child != 'N/A':
            fami[key] = {'hus_fam': [], 'wife_fam': [], 'hus_par': set(), 'wife_par': set(), 'family': family}
            for i in husband.child:
                fami[key]['hus_fam'].append(i[0])

            for i in wife.child:
                fami[key]['wife_fam'].append(i[0])

    for key, family in fam.items():

        for i, j in fami.items():

            if key in j['hus_fam']:
                j['hus_par'].add(family.husband[0].indi_id)
                j['hus_par'].add(family.wife[0].indi_id)

            if key in j['wife_fam']:
                j['wife_par'].add(family.husband[0].indi_id)
                j['wife_par'].add(family.wife[0].indi_id)

    global iserror
    for key, value in fami.items():

        for num in value['wife_par']:

            if num in value['hus_par']:
                iserror=1
                new_error = GedcomError(("ANOMALY", "FAMILY", "US18", value['family'].id[1], key),
                                        f"Siblings should not marry one another")
                value['family'].error_list = new_error

                break
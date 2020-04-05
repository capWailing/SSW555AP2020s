"""
Author: Zhiqiang Hunag
date: 03/01/2020
"""

from gedcom_app.errors.gedcom_error import GedcomError


def first_cousin_should_not_marry_us19(fam):
    grandparents_family_id_lis = []
    for key, value in fam.items():
        hus_id = value.husband[0]
        wif_id = value.wife[0]
        hus_family = hus_id.child
        wif_family = wif_id.child

        if hus_family not in ['N/A', ''] and wif_family not in ['N/A', '']:
            for family_hus in hus_family:
                family1 = fam.get(family_hus[0])
                husband_father_id = family1.husband[0]
                husband_mother_id = family1.wife[0]
                father_child = husband_father_id.child
                mother_child = husband_mother_id.child
                for child in father_child:
                    if father_child not in ['N/A', '']:
                        grandparents_family_id_lis.append(child[0])
                for child in mother_child:
                    if mother_child not in ['N/A', '']:
                        grandparents_family_id_lis.append(child[0])

            for family_wif in wif_family:
                family2 = fam.get(family_wif[0])
                wife_father_id = family2.husband[0]
                wife_mother_id = family2.wife[0]
                father_child = wife_father_id.child
                mother_child = wife_mother_id.child
                for child in father_child:
                    if father_child not in ['N/A', '']:
                        grandparents_family_id_lis.append(child[0])
                for child in mother_child:
                    if mother_child not in ['N/A', '']:
                        grandparents_family_id_lis.append(child[0])

            if len(grandparents_family_id_lis) == set(grandparents_family_id_lis):
                grandparents_family_id_lis = []
            else:
                new_error = GedcomError(("Error", "FAMILY", "US19", value.id[1], key),
                                        f"First cousins marry one another happened in family {value.id[0]}")
                value.error_list = new_error
        else:
            continue


def unique_name_and_birthday_us23(indi):
    lis_individual = []
    for key, value in indi.items():
        name = value.name
        birthday = value.birthday
        lis_individual.append((name[0], birthday[0]))

    set_individual = set(lis_individual)
    if len(lis_individual) != len(set_individual):
        for item in set_individual:
            lis_individual.remove(item)

        set_individual = set(lis_individual)
        for i in set_individual:
            for key, value in indi.items():
                if value.name[0] == i[0]:
                    new_error = GedcomError(("Error", "INDIVIDUAL", "US23", value.name[1], key),
                                            f"more than one individual with same name {value.name[0]} and birth date " +
                                            f"{value.birthday[0]} appear in the GED file")
                    value.error_list = new_error

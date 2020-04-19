"""
    author: Zituo Yan
    description: Corresponding entries
    date: 19/04/2020
"""
from gedcom_app.errors.gedcom_error import GedcomError


def indi_corresponding_in_family(indi, fam):
    for key, value in fam.items():
        husband = value.husband[0]
        wife = value.wife[0]
        children = value.children
        if value.husband != "N/A":
            check_existence_in_family(husband, "husband", indi, key, value, 0)
        if value.wife != "N/A":
            check_existence_in_family(wife, "wife", indi, key, value, 0)
        if value.children != "N/A":
            for offset, child in enumerate(children):
                check_existence_in_family(child, "child", indi, key, value, offset)


def check_existence_in_family(role, type, indi, key, value, offset):
    if role.indi_id[0] not in indi.keys():
        new_error = GedcomError(("Error", "Family", "US26", role.husband[1], key),
                                f"Corresponding issue happened. {role.indi_id[0]} not found in individual list.")
        value.error_list = new_error
    elif key not in [id_tuple[0] for id_tuple in indi[role.indi_id[0]].spouse] and type == "husband":
        new_error = GedcomError(("Error", "Family", "US26", value.husband[1], key),
                                f"Corresponding issue happened. Family {key}'s spouse "
                                f"{role.indi_id[0]} has wrong family Id.")
        value.error_list = new_error
    elif key not in [id_tuple[0] for id_tuple in indi[role.indi_id[0]].spouse] and type == "wife":
        new_error = GedcomError(("Error", "Family", "US26", value.wife[1], key),
                                f"Corresponding issue happened. Family {key}'s spouse "
                                f"{role.indi_id[0]} has wrong family Id.")
        value.error_list = new_error
    elif key not in [id_tuple[0] for id_tuple in indi[role.indi_id[0]].child] and type == "child":
        new_error = GedcomError(("Error", "Family", "US26", value.wife[1] + 1, key),
                                f"Corresponding issue happened. Family {key}'s children "
                                f"{role.indi_id[0]} has wrong family Id.")
        value.error_list = new_error


def family_corresponding_in_indi(indi, fam):
    for key, value in indi.items():
        if value.child != "N/A":
            check_existence_in_indi(value.child, "child", fam, key, value)
        if value.spouse != "N/A":
            check_existence_in_indi(value.spouse, "spouse", fam, key, value)


def check_existence_in_indi(family_id_list, type, fam, key, value):
    for offset, family_id in enumerate([id_tuple[0] for id_tuple in family_id_list]):
        if family_id not in fam.keys():
            new_error = GedcomError(("Error", "Individual", "US26", family_id_list[offset][1], key),
                                    f"Corresponding issue happened. {family_id} not found in family list.")
            value.error_list = new_error
        elif type == "child" and key not in [child.indi_id[0] for child in fam[family_id].children]:
            new_error = GedcomError(("Error", "Individual", "US26", family_id_list[offset][1], key),
                                    f"Corresponding issue happened. Family {family_id} does not have individual {key}.")
            value.error_list = new_error
        elif type == "spouse" and (key != fam[family_id].husband[0].indi_id[0] and key != fam[family_id].wife[0].indi_id[0]):
            new_error = GedcomError(("Error", "Individual", "US26", family_id_list[offset][1], key),
                                    f"Corresponding issue happened. Family {family_id} does not have individual {key}.")
            value.error_list = new_error

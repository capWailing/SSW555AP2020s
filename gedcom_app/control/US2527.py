"""
US2527
Author: Xinyi Ye
Date: 03.26.2020
"""


from gedcom_app.errors.gedcom_error import GedcomError
from collections import defaultdict

"""
Note: US27(Include individual ages) is implemented in view.output_prettytable.py
"""


def unique_first_names_in_families_us25(fam):
    """
    US25: Unique first names in families
    """
    for key, value in fam.items():
        dict_c_name = defaultdict(lambda: [])
        if value.children == ['N/A']:
            continue
        else:
            for child in value.children:
                id_c = child.indi_id[0]
                name_c = child.name
                first_name_c = name_c[0].split(' ')[0]
                if not dict_c_name[first_name_c]:
                    dict_c_name[first_name_c] = [id_c, name_c[1]]
                else:
                    l_id = dict_c_name[first_name_c]
                    l_id.extend([id_c, name_c[1]])
                    dict_c_name[first_name_c] = l_id

            for name1,value1 in dict_c_name.items():
                if len(value1) != 2:
                    l_child = []
                    for n in range(0, len(value1), 2):
                        l_child.append(value1[n])
                    new_error = GedcomError(("ANOMALY", "FAMILY", "US25", value1[1], key),
                                            f"children {l_child} of family {key} have the same first name '{name1}'")
                    value.error_list = new_error
                else:
                    continue



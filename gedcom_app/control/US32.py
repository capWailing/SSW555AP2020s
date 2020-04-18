"""
US32: list multiple birth
Author: Xinyi Ye
Date: 04/10/2020
"""
from collections import defaultdict
from prettytable import PrettyTable


def list_multiple_birth_us32(fam):
    """
    US32: List all multiple births in a GEDCOM file
    """
    l_multiple_birth = []
    for key, value in fam.items():
        if value.children == ['N/A']:
            continue
        else:
            dict = defaultdict(lambda: [])
            for child in value.children:
                id_c = child.indi_id[0]
                birth_c = child.birthday[0]
                l_tem = dict[birth_c]
                l_tem.append(id_c)
                dict[birth_c] = l_tem
            for item in dict.values():
                if len(item) != 1:
                    l_multiple_birth.append(item)
                else:
                    continue
    return l_multiple_birth  # list of id who has the same birth date within a family


def list_multiple_birth_us32_prettytable(indi, fam):
    l = list_multiple_birth_us32(fam)
    if l:
        for item in l:
            table_list_multiple_birth = PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death',
                                                 'Child', 'Spouse', 'Age'])
            for id in item:
                for key1, value1 in indi.items():
                    if key1 == id:
                        table_list_multiple_birth.add_row([id, value1.name[0],"Male" if value1.gender[0] == "M" else "Female",
                                                      value1.birthday[0], value1.alive,
                                                       value1.death if value1.death == "N/A" else value1.death[0],
                                                      [c[0] for c in value1.child] if value1.child != "N/A" else value1.child,
                                                      [s[0] for s in value1.spouse] if value1.spouse != "N/A" else value1.spouse,
                                                       value1.age])
                    else:
                        continue
            print("US32: list multiple birth")
            print(table_list_multiple_birth)










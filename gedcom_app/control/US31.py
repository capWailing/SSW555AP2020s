"""
US31:List living single
Author: Xinyi Ye
Date: 04/09/2020
"""
from prettytable import PrettyTable


def list_living_single_us31(indi):
    """
    US31: List all living people over 30 who have never been married
    """
    list_living_single = []
    for key, value in indi.items():
        if value.death == "N/A":
            if value.age > 30:
                if value.spouse == 'N/A':
                    list_living_single.append(key)
                else:
                    continue
            else:
                continue
        else:
            continue
    return list_living_single  # list of individual id of living people over 30 not married


def list_living_single_us31_prettytable(indi):
    """
    print all list living single person information in a prettytable
    """
    l = list_living_single_us31(indi)
    table_list_living_single = PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death', 'Child', 'Spouse', 'Age'])
    print("US31: List living single, list all living people over 30 who have never been married")
    for value in l:
        person = value
        for key1, value1 in indi.items():
            if key1 == person:
                table_list_living_single.add_row([person, value1.name[0],
                                                  "Male" if value1.gender[0] == "M" else "Female", value1.birthday[0],
                                                  value1.alive, "N/A", [c[0] for c in value1.child]
                                                  if value1.child != "N/A" else value1.child, "N/A", value1.age])
    print(table_list_living_single)








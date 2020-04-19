"""
    author: Zituo Yan
    description: list upcoming birthday in 30 days
    date: 19/04/2020
"""
from prettytable import PrettyTable
from datetime import datetime


def list_birthday_recent(indi):
    list_birth = []
    for key, value in indi.items():
        if value.death == "N/A" and if_birthday_close(datetime.strptime(value.birthday[0], "%d %b %Y")):
            list_birth.append(key)
    return list_birth


def if_birthday_close(birthday):
    current_date = datetime.now()
    return True if (current_date - birthday).days % 365.25 > 335 or (current_date - birthday).days == 0 else False


def list_recent_birth_prettytable(indi):
    """
    print all list living single person information in a prettytable
    """
    l = list_birthday_recent(indi)
    if l:
        table_list_living_single = PrettyTable(
            ['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death', 'Child', 'Spouse', 'Age'])
        print("US38: List all living people in a GEDCOM file whose birthdays occur in the next 30 days")
        for value in l:
            person = value
            for key1, value1 in indi.items():
                if key1 == person:
                    table_list_living_single.add_row([person, value1.name[0],
                                                      "Male" if value1.gender[0] == "M" else "Female",
                                                      value1.birthday[0],
                                                      value1.alive, "N/A", [c[0] for c in value1.child]
                                                      if value1.child != "N/A" else value1.child, "N/A",
                                                      value1.age])
        print(table_list_living_single)

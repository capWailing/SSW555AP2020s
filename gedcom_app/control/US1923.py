"""
Author: Zhiqiang Hunag
date: 03/01/2020
"""

from gedcom_app.errors.gedcom_error import GedcomError


def first_cousin_should_not_marry_us19(fam):
    grandchildren_list = []
    for key, value in fam.items():
        if len(value.children) >= 2:
            for children in value.children:
                children_child_ = children.child
                for children_child_id in range(len(children_child_id)):
                    grandchildren_list.append(indi.children_child_id)


                print(children_child_id)


def unique_date_and_birthday_us23(indi):
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

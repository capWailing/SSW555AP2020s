"""
    author: Zituo Yan, Xinyi Ye
    description:
    date: 04/01/2020
"""
from prettytable import PrettyTable


def individual_table(indi):
    """
    individual table
    + US27: Include individual ages
    """
    table_indi = PrettyTable(
        ['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death', 'Child', 'Spouse', 'Age'])
    for people in indi.values():
        table_indi.add_row([people.indi_id[0], people.name[0],
                           "Male" if people.gender[0] == "M" else "Female", people.birthday[0],
                            people.alive, people.death if people.death == "N/A" else people.death[0],
                            [c[0] for c in people.child] if people.child != "N/A" else people.child,
                            [s[0] for s in people.spouse] if people.spouse != "N/A" else people.spouse,
                            people.age])
    return table_indi


def family_table(fam):
    table_fam = PrettyTable(['ID', 'Married', 'Divorced', 'Husband ID',
                             'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
    for family in fam.values():
        table_fam.add_row([family.id[0], family.married[0],
                           family.divorced[0] if family.divorced != "N/A" else family.divorced,
                           family.husband[0].indi_id[0], family.husband[0].name[0], family.wife[0].indi_id[0],
                           family.wife[0].name[0], [child.indi_id[0] for child in family.children]
                           if len(family.children) != 0 else "N/A"])
    print(table_fam)
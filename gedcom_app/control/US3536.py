"""
author Zhiqiang Huang
date: 17/ 04/ 2020
"""

from prettytable import PrettyTable
import datetime


def recent_births(indi):
    """
    list all people in GEDCOM file who were born in the last 30 days
    """
    recent_births_list = []
    for key, value in indi.items():
        birthday = datetime.datetime.strptime(value.birthday[0], "%d %b %Y")
        today_before_30 = datetime.datetime.today() - datetime.timedelta(days=30)
        if today_before_30 <= birthday <= datetime.datetime.today():
            recent_births_list.append(key)
        else:
            continue

    return recent_births_list


def pretty_table_recent_births(indi):
    recent_births_list = recent_births(indi)
    if len(recent_births_list) > 0:
        table_list_recent_births = PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Alive',
                                                'Death', 'Child', 'Spouse', 'Age'])
        print("US35: list all people in GEDCOM file who were born in the last 30 days")
        for value in recent_births_list:
            person = value
            for key1, value1 in indi.items():
                if key1 == person:
                    table_list_recent_births.add_row([person,
                                                      value1.name[0],
                                                      "Male" if value1.gender[0] == "M" else "Female",
                                                      value1.birthday[0],
                                                      value1.alive,
                                                      value1.death if value1.death == 'N/A' else value1.death[0],
                                                      [c[0] for c in value1.child]if value1.child != "N/A" else value1.child,
                                                      [c[0] for c in value1.spouse]if value1.spouse != "N/A" else value1.spouse,
                                                      value1.age])
        print(table_list_recent_births)

    else:
        return None


def recent_deaths(indi):
    """
    list all people in GEDCOM file who died in the last 30 days
    """
    recent_death_list = []
    for key, value in indi.items():
        if value.death in ["N/A", '']:
            continue
        else:
            death_date = datetime.datetime.strptime(value.death[0], "%d %b %Y")
            today_before_30 = datetime.datetime.today() - datetime.timedelta(days=30)
            if today_before_30 <= death_date <= datetime.datetime.today():
                recent_death_list.append(key)
            else:
                continue
    return recent_death_list


def pretty_table_recent_death(indi):
    recent_death_list = recent_deaths(indi)
    if len(recent_death_list) > 0:
        table_list_recent_death = PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Alive',
                                               'Death', 'Child', 'Spouse', 'Age'])
        print("US36: list all people in GEDCOM file who death in the last 30 days")
        for value in recent_death_list:
            person = value
            for key1, value1 in indi.items():
                if key1 == person:
                    table_list_recent_death.add_row([person,
                                                     value1.name[0],
                                                    "Male" if value1.gender[0] == "M" else "Female", value1.birthday[0],
                                                     value1.alive,
                                                     value1.death if value1.death == 'N/A' else value1.death[0],
                                                     [c[0] for c in value1.child] if value1.child != "N/A" else value1.child,
                                                     [c[0] for c in value1.spouse]if value1.spouse != "N/A" else value1.spouse,
                                                     value1.age])
        print(table_list_recent_death)

    else:
        return None

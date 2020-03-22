"""
    author: Zituo Yan
    description: US 07 less than 150 years old
    date: 21/3/2020
"""
from datetime import timedelta, datetime

from gedcom_app.errors.gedcom_error import GedcomError


def less_than_150(indi):
    for key, people in indi.items():
        birthday = datetime.strptime(people.birthday[0], "%d %b %Y")
        deathday = ""
        if people.death != 'N/A':
            deathday = datetime.strptime(people.death[0], "%d %b %Y")
        if people.alive is False and birthday + timedelta(days=150*365) < deathday:
            new_error = GedcomError(("ERROR", "INDIVIDUAL", "US07", people.death[1], key),
                                    f"{people.name[0]}'s age should be less than 150 years.")
            people.error_list = new_error
        elif people.alive is True and birthday < datetime.today() - timedelta(days=150*365):
            new_error = GedcomError(("ERROR", "INDIVIDUAL", "US07", people.birthday[1], key),
                                    f"{people.name[0]} should no more than 150 years old.")
            people.error_list = new_error

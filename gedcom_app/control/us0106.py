"""
US0106
Author: boyu Wang
Date: 03/17/2020
"""

from datetime import datetime
from gedcom_app.errors.gedcom_error import GedcomError

today=datetime.today()


def date_before_current(indi,fam):
    for key, family in fam.items():

        marry_day=datetime.strptime(family.married[0],"%d %b %Y")
        if marry_day>today:
            new_error = GedcomError(("ERROR", "FAMILY", "US01", family.married[1], key),
                                    f"marry date {marry_day} before today")
            family.error_list = new_error

        if family.divorced[0] not in ['N/A','','N']:
            divor_day=datetime.strptime(family.divorced[0],"%d %b %Y")

            if divor_day>today:
                new_error = GedcomError(("ERROR", "FAMILY", "US01", family.divorced[1], key),
                                    f"divorce date {divor_day} before today")
                family.error_list = new_error

    for key,individual in indi.items():

        birth_day=datetime.strptime(individual.birthday[0],"%d %b %Y")
        if birth_day>today:
            new_error = GedcomError(("ERROR", "INDIVIDUAL", "US01", individual.birthday[1], key),
                                    f"birthday date {birth_day} before today")
            individual.error_list = new_error

        if individual.death[0] not in ['N/A', '', 'N']:
            death_day=datetime.strptime(individual.death[0],"%d %b %Y")

            if death_day>today:
                new_error = GedcomError(("ERROR", "INDIVIDUAL", "US01", individual.death[1], key),
                                    f"death date {death_day} before today")
                individual.error_list = new_error


def  div_before_death(fam):

    for key,family in fam.items():

        if family.divorced[0] not in ['N/A', '', 'N']:
            divor_day=datetime.strptime(family.divorced[0],"%d %b %Y")
            wife_death=family.wife[0].death[0]
            hus_death=family.husband[0].death[0]

            if wife_death[0] not in ['N/A', '', 'N']:
                wife_deathday=datetime.strptime(wife_death,"%d %b %Y")

                if wife_deathday<divor_day:
                    new_error = GedcomError(("ERROR", "FAMILY", "US06", family.divorced[1], key),
                                    f"divorce date {divor_day} after wife's death {wife_deathday}")
                    family.error_list = new_error

            if hus_death[0] not in ['N/A', '', 'N']:
                hus_deathday=datetime.strptime(hus_death,"%d %b %Y")

                if hus_deathday<divor_day:
                    new_error = GedcomError(("ERROR", "FAMILY", "US06", family.divorced[1], key),
                                    f"divorce date {divor_day} after husband's death {hus_deathday}")
                    family.error_list = new_error



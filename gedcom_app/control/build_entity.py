"""
    author: Zituo Yan
    description: build individual and family entity
    date: 2/3/2020
"""
from collections import defaultdict
from gedcom_app.entity.individual import Individual
from gedcom_app.entity.family import Family
from gedcom_app.errors.gedcom_error import GedcomError
from datetime import datetime

def build_individual(indi):
    indi_dict = defaultdict(Individual)
    for people in indi:
        if people["INDI"][0] in indi_dict.keys():
            new_error = GedcomError(("ERROR", "INDIVIDUAL", "US22", people["INDI"][1], people["INDI"][0]),
                                    f"Individual ID {people['INDI'][0]} should be unique!")
            indi_dict[people["INDI"][0]].error_list = new_error
        else:
            indi_birth_date = datetime.strptime(people["BIRTH"][0], "%d %b %Y")
            current_date = datetime.now()
            if people["DEAT"] == "N/A":
                num_date = current_date - indi_birth_date
                l_num_date = str(num_date).split(' ')
                age = int(float(l_num_date[0]) / 365.25)
            else:
                death_date = datetime.strptime(people["DEAT"][0], "%d %b %Y")
                num_date = death_date - indi_birth_date
                l_num_date = str(num_date).split(' ')
                age = f"death age: {int(float(l_num_date[0]) / 365.25)}"
            new_indi = Individual(people["INDI"], people["NAME"], people["SEX"],
                                  people["BIRTH"], people["DEAT"], people["FAMC"], people["FAMS"], age)
            indi_dict[people["INDI"][0]] = new_indi
    return indi_dict


def build_family(fam, indi_dict):
    fam_dict = defaultdict(Family)
    for family in fam:
        if family["FAM"][0] in fam_dict.keys():
            new_error = GedcomError(("ERROR", "FAMILY", "US22", family["FAM"][1], family["FAM"][0]),
                                    f"Family ID {family['FAM'][0]} should be unique!")
            fam_dict[family["FAM"][0]].error_list = new_error
        else:
            new_fam = Family(family["FAM"], family["MARR"], family["DIV"],
                             # add husband into family dictionary as an individual class
                             # which search from individual dictionary
                             (indi_dict[family["HUSB"][0]], family["HUSB"][1]),
                             (indi_dict[family["WIFE"][0]], family["WIFE"][1]))
            if family["CHIL"] != "N/A":
                for people in family["CHIL"]:
                    new_child = indi_dict[people[0]]
                    new_fam.children = new_child
            fam_dict[family["FAM"][0]] = new_fam
    return fam_dict

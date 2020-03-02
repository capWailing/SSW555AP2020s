"""
    author: Zituo Yan
    description: verify child's birthday
    date: 29/02/2020
"""
from datetime import datetime, timedelta


def birth_before_marriage(indi, fam):
    for key, value in fam.items():
        try:
            div_date = ""
            if value["DIV"][0] not in ['N', 'N/A']:
                div_date = datetime.strptime(value["DATE"][0], "%d %b %Y")
            marr_date = datetime.strptime(value["MARR"][0], "%d %b %Y")
        except KeyError:
            pass
        else:
            if value["CHIL"] != "N/A":
                for child in value["CHIL"]:
                    birth = datetime.strptime(indi[child[0]]["BIRTH"][0], "%d %b %Y")
                    if birth <= marr_date:
                        print(f"ANOMALY: FAMILY: US08: {indi[child[0]]['BIRTH'][1]}: {key}: "
                              f"Child {child[0]} born {birth} before marriage on {marr_date}")
                    elif value["DIV"] != "N/A" and birth > div_date + timedelta(days=270):
                        print(f"ANOMALY: FAMILY: US08: {indi[child[0]]['BIRTH'][1]}: {key}: "
                              f"Child {child[0]} born {birth} after divorce on {div_date}")

                    if indi[value["WIFE"][0]]["DEAT"] != "N/A":
                        mom_death = datetime.strptime(indi[value["WIFE"][0]]["DATE"][0], "%d %b %Y")
                        if birth > mom_death:
                            print(f"ANOMALY: FAMILY: US09: {indi[child[0]]['BIRTH'][1]}: {key}: "
                                  f"Child {child[0]} born {birth} after mother's death on {mom_death}")

                    if indi[value["HUSB"][0]]["DEAT"] != "N/A":
                        dad_death = datetime.strptime(indi[value["HUSB"][0]]["DATE"][0], "%d %b %Y")
                        if birth > dad_death + timedelta(days=270):
                            print(f"ANOMALY: FAMILY: US09: {indi[child[0]]['BIRTH'][1]}: {key}: "
                                  f"Child {child[0]} born {birth} after daddy's death on {dad_death}")

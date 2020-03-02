"""
    author: Zituo Yan
    description: verify child's birthday
    date: 29/02/2020
"""
from datetime import datetime, timedelta


def birth_before_marriage(fam):
    for key, family in fam.items():
        div_date = ""
        marr_date = datetime.strptime(family.married[0], "%d %b %Y")
        if_div = False
        if family.divorced != "N/A":
            div_date = datetime.strptime(family.divorced[0], "%d %b %Y")
            if_div = True

        for child in family.children:
            birth = datetime.strptime(child.birthday[0], "%d %b %Y")
            bir_line = child.birthday[1]
            child_id = child.indi_id[0]
            if birth <= marr_date:
                print(f"ANOMALY: FAMILY: US08: {bir_line}: {key}: "
                      f"Child {child_id} born {birth} before marriage on {marr_date}")
            elif if_div and birth > div_date + timedelta(days=270):
                print(f"ANOMALY: FAMILY: US08: {bir_line}: {key}: "
                      f"Child {child_id} born {birth} after divorce on {div_date}")

            if family.wife[0].death != "N/A":
                mom_death = datetime.strptime(family.wife[0].death[0], "%d %b %Y")
                if birth > mom_death:
                    print(f"ANOMALY: FAMILY: US09: {bir_line}: {key}: "
                          f"Child {child_id} born {birth} after mother's death on {mom_death}")

            if family.husband[0].death != "N/A":
                dad_death = datetime.strptime(family.husband[0].death[0], "%d %b %Y")
                if birth > dad_death + timedelta(days=270):
                    print(f"ANOMALY: FAMILY: US09: {bir_line}: {key}: "
                          f"Child {child_id} born {birth} after daddy's death on {dad_death}")

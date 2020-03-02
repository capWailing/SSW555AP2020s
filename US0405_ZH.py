"""
US0406
Author: Zhiqiang Huang
Date: 02/27/2020
"""
from datetime import datetime


def US04(fam):

    for key, value in fam.items():

        div = value['DATE']
        mar = value['MARR']
        if div in ('N/A', ''):
            continue

        else:
            if mar in ('N/A', ''):
                raise ValueError(f"Lost:{value['ID']} family marriage date lost")

            else:
                div_date = datetime.strptime(div[0], "%d %b %Y")
                mar_date = datetime.strptime(mar[0], "%d %b %Y")
                if div_date < mar_date:
                    print(f"Error: FAMILY: US04: {value['DATE'][1]}: {key}: Divorced {div[0]} before married {mar[0]}")


def US05(indi, fam):
    for key, value in fam.items():

        mar = value['MARR'][0]

        if mar in {'N/A', ''}:
            raise ValueError(f"Lost:{value['ID']} family marriage date lost")

        else:
            mar_date = datetime.strptime(mar, "%d %b %Y")
            hus_id = value['HUSB'][0]
            wif_id = value['WIFE'][0]
            hus_death = indi[hus_id]['DATE']
            wif_death = indi[wif_id]['DATE']

            if hus_death not in ('N/A', ''):
                hus_death_date = datetime.strptime(hus_death[0], "%d %b %Y")
                if hus_death_date < mar_date:
                    print(f"Error: FAMILY: US05: {value['MARR'][1]}: {key}: Married {mar} after husband's ({hus_id}) death on {hus_death[0]}")

            elif wif_death not in ('N/A', ''):
                wif_death_date = datetime.strptime(wif_death[0], "%d %b %Y")
                if wif_death_date < mar_date:
                    print(f"Error: FAMILY: US05: {value['MARR'][1]}: {key}: Married {mar} after wife's ({wif_id}) death on {wif_death[0]}")

            else:
                continue

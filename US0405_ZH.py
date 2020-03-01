"""
US0406
Author: Zhiqiang Huang
Date: 02/27/2020
"""
from datetime import datetime


def US04(fam):

    for key, value in fam.items():

        div = value['DATA'][0]
        mar = value['MARR'][0]

        if div in ('N/A', ''):
            continue

        else:
            if mar in ('N/A', ''):
                raise ValueError(f"Lost:{value['ID']} family marriage date lost")

            else:
                div_date = datetime.strptime(div, "%d %b %Y")
                mar_date = datetime.strptime(mar, "%d %b %Y")
                if div_date < mar_date:
                    print(f"Error: FAMILY: US04 {value['DATA'][1]}: {key}: Divorced {div_date} before married {mar_date}")


def US05(indi, fam):
    for key, value in fam.items():

        mar = value['MARR'][0]

        if mar in {'N/A', ''}:
            raise ValueError(f"Lost:{value['ID']} family marriage date lost")

        else:
            mar_date = datetime.strptime(mar, "%d %b %Y")
            hus_death = indi[value['HUBS'][0]]['DATE']
            wif_death = indi[value['WIFE'][0]]['DATE']

            if hus_death not in ('N/A', ''):
                hus_death_date = datetime.strptime(hus_death, "%d %b %Y")
                if hus_death_date < mar_date:
                    print(f"Error: US05; {value['MARR'][1]}: {key}: Married {mar_date} after husband's ({value['HUBS'][0]}) death on {hus_death_date}")

            elif wif_death not in ('N/A', ''):
                wif_death_date = datetime.strptime(wif_death, "%d %b %Y")
                if wif_death_date < mar_date:
                    print(f"Error: US05: {value['MARR'][1]}: {key}: Married {mar_date} after wife's ({value['WIFE'][0]}) death on {wif_death_date}")

            else:
                continue

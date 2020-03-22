"""
US0406
Author: Zhiqiang Huang
Date: 02/27/2020
"""
from datetime import datetime
from gedcom_app.errors.gedcom_error import GedcomError


def USO4(fam):
    for key, value in fam.items():

        date_divorced = value.divorced
        date_married = value.married
        if date_divorced in ('N/A', ''):
            continue

        else:
            if date_married in ('N/A', ''):
                raise ValueError(f"Lost:{value.id[0]} family marriage date lost")

            else:
                div_date = datetime.strptime(date_divorced[0], "%d %b %Y")
                mar_date = datetime.strptime(date_married[0], "%d %b %Y")
                if div_date < mar_date:
                    new_error = GedcomError(("Error", "FAMILY", "US04", date_divorced[1], key),
                                            f"Divorced {date_divorced[0]} before married {date_married[0]}")
                    value.error_list = new_error


def US05(fam):
    for key, value in fam.items():

        date_married = value.married

        if date_married in {'N/A', ''}:
            raise ValueError(f"Lost:{value.id[0]} family marriage date lost")

        else:
            mar_date = datetime.strptime(date_married[0], "%d %b %Y")
            hus_id = value.husband[0]
            wif_id = value.wife[0]
            hus_death = hus_id.death
            wif_death = wif_id.death

            if hus_death not in ('N/A', ''):
                hus_death_date = datetime.strptime(hus_death[0], "%d %b %Y")
                if hus_death_date < mar_date:
                    new_error = GedcomError(("Error", "FAMILY", "US05", date_married[1], key),
                                            f"Married {date_married[0]} after husband's ({hus_id.indi_id[0]}) death on {hus_death[0]}")
                    value.error_list = new_error

            elif wif_death not in ('N/A', ''):
                wif_death_date = datetime.strptime(wif_death[0], "%d %b %Y")
                if wif_death_date < mar_date:
                    new_error = GedcomError(("Error", "FAMILY", "US05", datetime[1], key),
                                            f"Married {date_married[0]} after wife's ({wif_id.indi_id[0]}) death on {wif_death[0]}")
                    value.error_list = new_error

            else:
                continue
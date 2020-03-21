"""
US11
Author: Zhiqiang Huang
Date: 03/18/2020
"""
from datetime import datetime
from gedcom_app.errors.gedcom_error import GedcomError


def US11(indi, fam):
    for key, value in indi.items():
        lis_spouse = value.spouse
        if len(lis_spouse) > 1 and lis_spouse not in ['N/A', '']:
            for i in range(len(lis_spouse)):
                fam_id_1 = lis_spouse[i][0]
                date_married_1 = fam[fam_id_1].married
                marriage_date_1 = datetime.strptime(date_married_1[0], "%d %b %Y")
                date_divorced_1 = fam[fam_id_1].divorced

                if date_divorced_1 in ('N/A', ''):
                    divorced_date_1 = datetime.strptime('21 MAR 2020', "%d %b %Y")
                else:
                    divorced_date_1 = datetime.strptime(date_divorced_1[0], "%d %b %Y")

                for j in range(i+1, len(lis_spouse)):
                    fam_id_2 = lis_spouse[j][0]
                    date_married_2 = fam[fam_id_2].married
                    marriage_date_2 = datetime.strptime(date_married_2[0], "%d %b %Y")
                    divorced_date_2 = fam[fam_id_2].divorced

                    if divorced_date_2 in ('N/A', ''):
                        divorced_date_2 = datetime.strptime('21 MAR 2020', "%d %b %Y")
                    else:
                        divorced_date_2 = datetime.strptime(divorced_date_2[0], "%d %b %Y")


                    if marriage_date_1 >= divorced_date_2 or marriage_date_2 >= divorced_date_1:
                        continue
                    else:
                        new_error = GedcomError(("Error", "INDIVIDUAL", "US11", date_married_1[1], key),
                                                f"bigamy happened on family {fam_id_1} and family {fam_id_2}")
                        value.error_list = new_error

        else:
            continue

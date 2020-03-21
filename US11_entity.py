"""
US0406
Author: Zhiqiang Huang
Date: 02/27/2020
"""
from datetime import datetime
from collections import defaultdict
from unittest import TestCase
import unittest


def parse_GEDCOM(path):
    """
    parse_GEDCOM() funtion:
    parse .ged file to collect all data into dict_indi dictionary and dict_fam dictionary
    """

    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"can not open this path")
    else:
        with fp:

            dict_indi = {}
            dict_fam = {}
            """
            dicy_indi, dict_fam dictionaries: collect the results of data in .ged file
            """
            child_s = []
            famc_s = []
            fams_s = []
            """
            child_s sets: collect children in FAM level,
            famc_s, fams_s sets: collect children and spouses in INDI level
            """
            num = 0
            list = []
            sum = []
            date_b = 0
            """
            num: record the number of 'INDI' and 'FAM' as a parameter
            list: temporary list to add data into sum
            sum: collect all datas into sum list
            date_b : a variable to record number of 'DATE', it is used to judge 'BIRT' or 'DEAT', 'MARR' or 'DIV'
            """
            feat_IND = defaultdict(lambda: 'N/A')
            feat_FAM = defaultdict(lambda: 'N/A')
            """
            feat_IND, feat_FAM are defaultdict, the default value is 'N/A'
            used to record characteristics of INDI and FAM excepting ID
            """
            line_num = 0
            for line in fp:
                line_num += 1
                line = line.rstrip('\n').rstrip(' ')
                list_line = line.split(' ')
                level = list_line[0]

                if level == '0':
                    s_tag = list_line[len(list_line) - 1]
                    """ s_tag: the last word in the line, it used to judge 'INDI' or 'FAM"""
                    del list_line[0]
                    del list_line[len(list_line) - 1]
                    ID = ' '.join(list_line)
                    """ ID: argument"""

                    if num == 0:
                        """
                        num: record the number of 'INDI' and 'FAM' as a parameter
                        """
                        if s_tag == 'INDI':
                            num += 1
                            line_ID = line_num
                            list.append(['INDI', ID, line_ID])
                        elif s_tag == 'FAM':
                            num += 1
                            line_ID = line_num
                            list.append(['FAM', ID, line_ID])
                        line_ID = 0
                    else:
                        """
                        num != 0 which means there is already an 'INDI' or 'FAM'
                        when level == 0, it means an INDI or FAM is finished
                        """
                        num += 1
                        if num == 2:
                            """ an INDI or FAM is finished"""
                            sum.append(list)
                            list = []

                            if s_tag == 'INDI':
                                num = 1
                                line_ID = line_num
                                list.append(['INDI', ID, line_ID])

                            elif s_tag == 'FAM':
                                num = 1
                                line_ID = line_num
                                list.append(['FAM', ID, line_ID])
                            else:
                                num = 0
                            line_ID = line_num
                elif level != '0':
                    tag = list_line[1]
                    del list_line[0: 2]
                    argument = ' '.join(list_line)
                    if tag == 'BIRT':
                        date_b = 1
                    elif tag == 'MARR':
                        date_b = 2
                    elif date_b == 1:
                        if tag == 'DATE':
                            """ date_b == 1 which means it is birth date """
                            line_BIRTH = line_num
                            list.append(['BIRTH', argument, line_BIRTH])
                        else:
                            line_BIRTH = line_num - 1

                            list.append(['BIRTH', '', line_BIRTH])
                            list.append([tag, argument, line_num])
                        date_b = 0
                    elif date_b == 2:
                        if tag == 'DATE':
                            """ date_b == 2 which means it is married date"""
                            list.append(['MARR', argument, line_num])
                        else:
                            list.append(['MARR', '', line_num - 1])
                            list.append([tag, argument, line_num])
                        date_b = 0
                    else:
                        list.append([tag, argument, line_num])
                        date_b = 0

            if level != '0':
                """
                whis situation is INDI or FAM ends without accompanying level 0
                """
                sum.append(list)

            for item in sum:

                if item[0][0] == 'INDI':
                    feat_IND['line_ID'] = item[0][2]
                    m = item.pop(0)

                    for q in item:
                        if q[0] == 'FAMC':

                            famc_s.append([q[1], q[2]])

                            feat_IND['FAMC'] = famc_s
                            """
                            collect famc in indi level and put them into famc_s set
                            """
                        elif q[0] == 'FAMS':

                            fams_s.append([q[1], q[2]])
                            feat_IND['FAMS'] = fams_s
                            """
                            collect fams in indi level and put them into fams_s set
                            """
                        else:
                            feat_IND[q[0]] = [q[1], q[2]]

                    dict_indi[m[1]] = feat_IND
                    """ put feat_IND into the result dictionary dict_indi """
                    famc_s = []
                    fams_s = []
                    feat_IND = defaultdict(lambda: 'N/A')

                elif item[0][0] == 'FAM':
                    feat_FAM['line_ID'] = item[0][2]
                    n = item.pop(0)
                    for q in item:
                        if q[0] == 'CHIL':

                            child_s.append([q[1], q[2]])
                            feat_FAM['CHIL'] = child_s
                            """
                            collect children in fam level and put them into child_s set
                            """
                        else:
                            feat_FAM[q[0]] = [q[1], q[2]]

                    dict_fam[n[1]] = feat_FAM
                    """ put feat_FAM into the result dictionary dict_fam """
                    child_s = []
                    feat_FAM = defaultdict(lambda: 'N/A')

            if len(dict_indi) < 5000 and len(dict_fam) < 1000:
                return dict_indi, dict_fam
            else:
                raise ValueError(f"Data overflow")


def USO4(fam):
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


def US11(indi, fam):
    for key, value in indi.items():
        if len(value["FAMS"]) > 1 and value['FAMS'] not in ['N/A', '']:
            for i in range(len(value['FAMS'])):
                fam_id_1 = value['FAMS'][i][0]
                date_married_1 = fam[fam_id_1]['MARR']
                marriage_date_1 = datetime.strptime(date_married_1[0], "%d %b %Y")
                date_divorced_1 = fam[fam_id_1]['DATE']
                if date_divorced_1 in ('N/A', ''):
                    divorced_date_1 = datetime.strptime('21 MAR 2020', "%d %b %Y")
                    print(1)
                else:
                    divorced_date_1 = datetime.strptime(date_divorced_1[0], "%d %b %Y")
                for j in range(i+1, len(value['FAMS'])):
                    fam_id_2 = value['FAMS'][j][0]
                    date_married_2 = fam[fam_id_2]['MARR']
                    marriage_date_2 = datetime.strptime(date_married_2[0], "%d %b %Y")
                    divorced_date_2 = fam[fam_id_2]['DATE']
                    if divorced_date_2 in ('N/A', ''):
                        divorced_date_2 = datetime.strptime('21 MAR 2020', "%d %b %Y")
                        print(2)
                    else:
                        divorced_date_2 = datetime.strptime(divorced_date_2[0], "%d %b %Y")

                    if marriage_date_1 >= divorced_date_2 or marriage_date_2 >= divorced_date_1:
                        continue
                    else:
                        return (f'Error: INDIVIDUAL: US11: {date_married_1[1]}: {key}: bigamy '
                              f'happened on family {fam_id_1} and family {fam_id_2}')


class Test(TestCase):

    def test_US11(self):
        indi, fam = parse_GEDCOM('test_US0405.ged')
        self.assertEqual(US11(indi, fam), 'Error: INDIVIDUAL: US11: 61: I04: bigamy happened on family F2 and family F3')


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

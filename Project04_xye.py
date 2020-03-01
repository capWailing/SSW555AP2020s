"""
project04
Author:Xinyi Ye, Boyu Wang
Date: 02.27.2020
"""
from prettytable import PrettyTable
from collections import defaultdict
import US0203_xye
import US0106_wby


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
                    s_tag = list_line[len(list_line)-1]
                    """ s_tag: the last word in the line, it used to judge 'INDI' or 'FAM"""
                    del list_line[0]
                    del list_line[len(list_line)-1]
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
                            list.append(['MARR', '', line_num -1])
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
            
            for key, value in dict_fam.items():
                l_item1 = []   
                if value['DATE'] != 'N/A':
                    l_child = value['CHIL']
                    id_wife = value['WIFE'][0]
                    id_hus = value['HUSB'][0] 
                    fam_key = key
                    
                    for key1, value1 in dict_fam.items():
                        if value1['HUSB'][0] == id_hus or value1['WIFE'][0] == id_wife:
                            if key1 != fam_key:
                                for item1 in value1['CHIL']:
                                    l_item1.append(item1[0]) 
                                for item in l_child:
                                    if item[0] not in l_item1:
                                        value1['CHIL'].append(item)
                                    else:
                                        continue
                                dict_fam[key1]['CHIL'] = value1['CHIL']

            for key2, value2 in dict_indi.items():
                l_item2 = []
                if value2['DATE'] != 'N/A' :
                    id_death = key2 
                    for fam in value2['FAMS']:
                        key_fam = fam[0]
                        child = dict_fam[key_fam]['CHIL']
                        for key4, value4 in dict_fam.items():
                            if id_death == dict_fam[key_fam]['HUSB'][0]:
                                if dict_fam[key_fam]['WIFE'][0] in [value4['HUSB'][0], value4['WIFE'][0]] and key4 != key_fam:
                                    for item1 in value4['CHIL']:
                                        l_item2.append(item1[0])
                                    for item in child :
                                        if item[0] not in l_item2:
                                            value4['CHIL'].append(item)
                                        else:
                                            continue
                                    dict_fam[key4]['CHIL'] = value4['CHIL']

                            elif id_death == dict_fam[key_fam]['WIFE']:
                               
                                if dict_fam[key_fam]['HUSB'][0] in [value4['HUSB'][0], value4['WIFE'][0]] and key4 != key_fam:
                                    for item1 in value4['CHIL']:
                                        l_item2.append(item1[0])
                                    for item in child :
                                        if item[0] not in l_item2:
                                            value4['CHIL'].append(item)
                                        else:
                                            continue
                                    dict_fam[key4]['CHIL'] = value4['CHIL']
                else:
                    continue  
            
            if len(dict_indi) < 5000 and len(dict_fam) < 1000:
                return dict_indi, dict_fam
            else:
                raise ValueError(f"Data overflow")


if __name__ == "__main__":
    """ 
    main() function: input path, print two tables
    if data lost, it will display '' in table
    if no record of items, it will display'N/A'
    """
    path = input("please input the .ged file path:")
    try:
        indi, fam = parse_GEDCOM(path)
    except FileNotFoundError as e:
        print(e)
    except ValueError as m:
        print(m)
    else:
        
        table_indi = PrettyTable(
            ['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death', 'Child', 'Spouse'])
        table_fam = PrettyTable(['ID', 'Married', 'Divorced', 'Husband ID',
                                 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
        l_FAMC = []
        l_FAMS = []
        l_CHIL = []
        famc = 'N/A'
        fams = 'N/A'
        chil = 'N/A'
        
        for key, value in indi.items():  
            DATE_DEATH = 'N/A'       
            if value['DEAT'] == 'N/A':
                alive = 'TRUE'
            else:
                if value['DATE'][0] not in ['', 'N']:
                    alive = 'FALSE'
                    DATE_DEATH = value['DATE'][0]
                else:   
                    alive = 'FALSE'
                    DATE_DEATH = ''
            
            if value['FAMC'] == 'N/A':
                famc = 'N/A'
            else:    
                for famc in value['FAMC']:
                    l_FAMC.append(famc[0])
                famc = l_FAMC
            
            if value['FAMS'] == 'N/A':
                fams = 'N/A'
            else:
                for fams in value['FAMS']:
                    l_FAMS.append(fams[0]) 
                fams = l_FAMS
            
            table_indi.add_row([key, value['NAME'][0], value['SEX'][0], value['BIRTH'][0],
                                alive, DATE_DEATH, famc, fams])
            l_FAMC = []
            l_FAMS = []

        for key, value in fam.items():

            DATE_DIV = 'N/A' 
            id_h = value['HUSB'][0]
            id_w = value['WIFE'][0]
            """ husband id and wife id """
            if id_h not in ['N', '']:
                name_h = indi[id_h]['NAME'][0]
            else:
                name_h = 'N/A'
            """ get husband's name"""
            if id_w not in['N', '']:
                name_w = indi[id_w]['NAME'][0]
            else:
                name_w = 'N/A'
            """ get wife's name"""

            if value['DIV'] == 'N/A':
                
                DATE_DIV = 'N/A'
            else:
                if value['DATE'][0] in ['', 'N']:
                    DATE_DIV = ''
                else:
                    DATE_DIV = value['DATE'][0]
            """ 
            if div record lost, print''
            if no divorce, print'N/A'
            """
            
            if value['CHIL'] == 'N/A':
                chil = 'N/A'
            else:
                for chil in value['CHIL']:
                    l_CHIL.append(chil[0]) 
                chil = l_CHIL
            table_fam.add_row([key, value['MARR'][0], DATE_DIV,
                               id_h, name_h, id_w, name_w, chil])
        
            l_CHIL = []
        
        print(table_indi)
        print(table_fam)

        try:
            US0203_xye.US02(indi, fam)
        except ValueError as e:
            print(e)
        try:
            US0203_xye.US03(indi)
        except ValueError as e:
            print(e)

        try:
            US0106_wby.US01(indi, fam)
        except ValueError as e:
            print(e)
        try:
            US0106_wby.US06(indi, fam)
        except ValueError as e:
            print(e)

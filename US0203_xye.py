"""
US0203
Author: Xinyi Ye
Date: 02/26/2020
"""
from datetime import datetime, timedelta

def US02(indi, fam):
        
    for key, value in fam.items():
           
        marriage_date = datetime.strptime(value['MARR'][0], "%d %b %Y")
        id_h = value['HUSB'][0]
        id_w = value['WIFE'][0]
            
        if id_h not in ['N/A', '']:
            birth_h = indi[id_h]['BIRTH']
            if birth_h != 'N/A' and birth_h[0] != '':
                h_birth_date = datetime.strptime(birth_h[0], "%d %b %Y")
            else:
                raise ValueError(f"Lost: {id_h} birth lost")
        else:
             raise ValueError(f"Lost: {key} family husband id lost")
        if id_w not in['N/A', '']:
            birth_w = indi[id_w]['BIRTH']
            if birth_w != 'N/A' and birth_w[0] != '':
                w_birth_date = datetime.strptime(birth_w[0], "%d %b %Y")
            else:
                raise ValueError(f"Lost: {id_w} birth lost")                
        else:
            raise ValueError(f"Lost: {key} family wife id lost")       
            
        if h_birth_date >= marriage_date:
            print(f"Error: FAMILY: US02 birth before marriage：line {birth_h[1]} and {value['MARR'][1]}: {id_h}: {birth_h[0]} isn't before {value['MARR'][0]}") 
        
        if w_birth_date >= marriage_date:
            print(f"Error: FAMILY: US02 birth before marriage：line {birth_w[1]} and {value['MARR'][1]}: {id_w}: {birth_w[0]} isn't before {value['MARR'][0]}") 
        else:
            continue

def US03(indi):
        
    for key, value in indi.items():
        birth = value['BIRTH']
        death = value['DATE']

        if value['DEAT'] != 'N/A':
            if death != 'N/A' and death[0] != '':
                death_date = datetime.strptime(death[0], "%d %b %Y")
            else:
                raise ValueError(f"Lost: {key} death data lost")
        else:
            continue
        if birth != 'N/A' and birth[0] != '':
            birth_date = datetime.strptime(birth[0], "%d %b %Y")
        else:
            raise ValueError(f"Lost: {key} birth data lost")

        if birth_date >= death_date:
            print(f"Error: INDIVITUAL: US03 birth before death：line {birth[1]} and {death[1]}: {key}: {birth[0]} isn't before {death[0]}") 
        else:
            continue
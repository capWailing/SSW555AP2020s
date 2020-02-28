"""
US12
Author: Xinyi Ye
Date: 02/26/2020
"""
from datetime import datetime

def US12(indi, fam):
    
    for key, value in fam.items():
        if value['CHIL'] == 'N/A':
            continue
        else:
            id_h = value['HUSB'][0]
            id_w = value['WIFE'][0]
            id_c = value['CHIL']
            
            for child in id_c:
                
                if child[0] == '':
                    raise ValueError(f"Lost: {key} family child data lost")
                else:
                    birth_h = indi[id_h]['BIRTH']
                    birth_w = indi[id_w]['BIRTH'] 
                    birth_c = indi[child[0]]['BIRTH']       
                        
                if birth_h == 'N/A' or birth_h[0] == '':
                    raise ValueError(f"Lost: {key} family father {id_h} birthday data lost")
                elif birth_w == 'N/A' or birth_w[0] == '':
                    raise ValueError(f"Lost: {key} family mother {id_w} birthday data lost")
                elif birth_c == 'N/A' or birth_c[0] == '':
                    raise ValueError(f"Lost: {key} family child {child[0]} birthday data lost")
                else:
                    h_birth_date = datetime.strptime(birth_h[0], "%d %b %Y")
                    w_birth_date = datetime.strptime(birth_w[0], "%d %b %Y")
                    c_birth_date = datetime.strptime(birth_c[0], "%d %b %Y")

                    num_hc = c_birth_date - h_birth_date
                    l_hc = str(num_hc).split(' ')
                    num_wc = c_birth_date - w_birth_date
                    l_wc = str(num_wc).split(' ')
                   
                    
                if int(l_hc[0]) >= 80 * 365.25:
                    print(f"Error: FAMILY: US12 Parents not too old: line {birth_h[1]} and {birth_c[1]}: father {id_h} {birth_h[0]} is not less than 80 years old than child {child[0]} {birth_c[0]}")
                
                
                if int(l_wc[0]) >= 60 * 365.25:
                    print(f"Error: FAMILY: US12 Parents not too old: line {birth_w[1]} and {birth_c[1]}: mother {id_w} {birth_w[0]} is not less than 60 years old than child {child[0]} {birth_c[0]}")
                else:
                    continue

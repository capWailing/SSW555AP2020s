from datetime import datetime

def US02(indi, fam):
        
    for key, value in fam.items():
           
        marriage_date = datetime.strptime(value['MARR'], "%d %b %Y")
        id_h = value['HUSB']
        id_w = value['WIFE']
            
        if id_h not in ['N/A', '']:
            birth_h = indi[id_h]['BIRTH']
            if birth_h not in ['N/A', '']:
                h_birth_date = datetime.strptime(birth_h, "%d %b %Y")
            else:
                raise ValueError(f"Lost: {id_h} birth lost")
        else:
             raise ValueError(f"Lost: {key} family husband id lost")
        if id_w not in['N/A', '']:
            birth_w = indi[id_w]['BIRTH']
            if birth_w not in ['N/A', '']:
                w_birth_date = datetime.strptime(birth_w, "%d %b %Y")
            else:
                raise ValueError(f"Lost: {id_w} birth lost")                
        else:
            raise ValueError(f"Lost: {key} family wife id lost")       
            
        if h_birth_date >= marriage_date:
            print(f"Error: FAMILY: US02 birth before marriage：{id_h}: {birth_h} isn't before {value['MARR']}") 
        
        if w_birth_date >= marriage_date:
            print(f"Error: FAMILY: US02 birth before marriage：{id_w}: {birth_w} isn't before {value['MARR']}") 
        else:
            continue

def US03(indi):
        
        for key, value in indi.items():
            birth = value['BIRTH']
            death = value['DATE']

            if value['DEAT'] != 'N/A':
                if death not in ['N/A', '']:
                    death_date = datetime.strptime(death, "%d %b %Y")
                else:
                    raise ValueError(f"Lost: {key} death data lost")
            else:
                continue
            if birth not in ['N/A', '']:
                birth_date = datetime.strptime(birth, "%d %b %Y")
            else:
                raise ValueError(f"Lost: {key} birth data lost")

            if birth_date >= death_date:
                print(f"Error: INDIVITUAL: US03 birth before death：{key}: {birth} isn't before {death}") 
            else:
                continue
from datetime import datetime
from datetime import datetime

def US01(indi):
        
    for key, value in indi.items():

        birstday=value['BIRTH']
        death=value['DATE']

        if birstday in ['N/A','']:
            raise ValueError(f"Lost: {value['NAME']} birth lost")      
        else:
            birstday_date = datetime.strptime(birstday, "%d %b %Y")
            if death not in ['N/A','']:
                death_date=datetime.strptime(death,"%d %b %Y")
                if birstday_date>death_date:
                    print(f"Error: INDI: US01 death before birth：{key}: death date {death} before birth date {birstday}")




def US06(indi,fam):

    for key,value in fam.items():


        if value['DATE'] not in ['N/A','']:
            husband_id=value["HUSB"]
            wife_id=value['WIFE']
            div_date=datetime.strptime(value['DATE'], "%d %b %Y")

            if husband_id in ['N/A',''] or wife_id in ['N/A','']:
                raise ValueError("lost: Husband's id or wife'id lost in this family.")

            husband_death=indi[husband_id]['DATE']
            wife_death=indi[wife_id]['DATE']

            if husband_death not in ['N/A','']:
                husb_death=datetime.strptime(husband_death, "%d %b %Y")
                if husb_death<div_date:
                    print(f"ERROR: FAMILY:US06 death before divorce: {husband_id}:death date {husband_death} before divorce date {value['DATE']}")

            elif wife_death not in ['N/A','']:
                wif_death=datetime.strptime(wife_death, "%d %b %Y")
                if wif_death<div_date:
                    print(f"ERROR: FAMILY:US06 death before divorce: {wife_id}:death date {wife_death} before divorce date {value['DATE']}")


        else:
            continue
        

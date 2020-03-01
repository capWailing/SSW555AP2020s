from datetime import datetime

def US01(indi,fam):
    
    today=datetime.today();
    for key, value in indi.items():

        birthday=value['BIRTH'][0]
        death=value['DATE'][0]

        if birthday in ['N/A','','N']:
            raise ValueError(f"Lost: {key}'s birth lost")      
        else:
            birthday_date = datetime.strptime(birthday, "%d %b %Y") 
            if birthday_date>today:
                    print(f"ERROR: INDIVIDUAL: US01: {value['BIRTH'][1]}:{key}: birth date {birthday} before today")

        if death not in ['N/A','','N']:
            death_date=datetime.strptime(death,"%d %b %Y")
            if death_date>today:
                    print(f"ERROR: INDIVIDUAL: US01: {value['DATE'][1]}:{key}: death date {birthday} before today")
               
    
    for key, value in fam.items():
        marry_day=value["MARR"][0]
        div_day=value['DATE'][0]

        if marry_day in ['N/A','','N']:
            raise ValueError(f"Lost: {key}'s marry date lost")      
        else:
            marry_date = datetime.strptime(marry_day, "%d %b %Y") 
            if marry_date>today:
                    print(f"ERROR: FAMILY: US01: {value['MARR'][1]}:{key}: marry date {marry_day} before today")

        if div_day not in ['N/A','','N']:
            div_date=datetime.strptime(div_day,"%d %b %Y")
            if div_date>today:
                    print(f"ERROR: FAMILY: US01: {value['DATE'][1]}:{key}: divorce date {div_day} before today")



def US06(indi,fam):

    for key,value in fam.items():

        if value['DATE'][0] not in ['N/A','','N']:
            husband_id=value["HUSB"][0]
            wife_id=value['WIFE'][0]
            div_date=datetime.strptime(value['DATE'][0], "%d %b %Y")

            if husband_id in ['N/A','','N'] or wife_id in ['N/A','',"N"]:
                raise ValueError("lost: Husband's id or wife'id lost in this family.")

            husband_death=indi[husband_id]['DATE'][0]
            wife_death=indi[wife_id]['DATE'][0]

            if husband_death not in ['N/A','',"N"]:
                husb_death=datetime.strptime(husband_death, "%d %b %Y")
                if husb_death<div_date:
                    print(f"ERROR: FAMILY: US06: {value['DATE'][1]}: {key}:hunsband's death date {husband_death} before divorce date {value['DATE'][0]}")

            if wife_death not in ['N/A','',"N"]:
                wif_death=datetime.strptime(wife_death, "%d %b %Y")
                if wif_death<div_date:
                    print(f"ERROR: FAMILY: US06: {value['DATE'][1]}: {key}:wife's death date {wife_death} before divorce date {value['DATE'][0]}")

        else:
            continue
        

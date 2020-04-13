from gedcom_app.errors.gedcom_error import GedcomError


def listalldeceased(indi):

    deathPeople = []
    for key, value in indi.items():
        if value.death[0] not in ['', 'N', 'N/A']:
            child=[]
            spouse=[]
            if value.child not in ['', 'N', 'N/A']:
                for i in value.child:
                    child.append(i[0])
            else:
                child.append(value.child)

            if value.spouse not in ['', 'N', 'N/A']:
                for i in value.spouse:
                    spouse.append(i[0])
            else:
                spouse.append(value.spouse)

            deathPeople.append(f'US29:ID:{value.indi_id[0]}; Name:{value.name[0]}; Gender:{value.gender[0]}; Birthday:{value.birthday[0]}; Death{value.death[0]}; Famc:{child}; Fams:{spouse}')
        else:
            continue
    return deathPeople


def listlivemarried(fam):

    livemarried=set()

    for key,value in fam.items():

        husband = value.husband[0]
        wife = value.wife[0]

        if husband.death[0] in ['', 'N', 'N/A']:
            childh=[]
            spouseh=[]
            if husband.child not in ['', 'N', 'N/A']:
                for i in husband.child:
                    childh.append(i[0])
            else:
                childh.append(husband.child)

            if husband.spouse not in ['', 'N', 'N/A']:
                for i in husband.spouse:
                    spouseh.append(i[0])
            else:
                spouseh.append(husband.spouse)
            livemarried.add(f'US30:ID:{husband.indi_id[0]}; Name:{husband.name[0]}; Gender:{husband.gender[0]}; Birthday:{husband.birthday[0]}; Death:{husband.death}; Famc:{childh}; Fams:{spouseh}')

        if wife.death[0] in ['', 'N', 'N/A']:
            childw=[]
            spousew=[]
            if wife.child not in ['', 'N', 'N/A']:
                for i in wife.child:
                    childw.append(i[0])
            else:
                childw.append(wife.child)

            if wife.spouse not in ['', 'N', 'N/A']:
                for i in wife.spouse:
                    spousew.append(i[0])
            else:
                spousew.append(wife.spouse)
            livemarried.add(f'US30:ID:{wife.indi_id[0]}; Name:{wife.name[0]}; Gender:{wife.gender[0]}; Birthday:{wife.birthday[0]}; Death:{wife.death}; Famc:{childw}; Fams:{spousew}')

        else:
            continue

    return livemarried


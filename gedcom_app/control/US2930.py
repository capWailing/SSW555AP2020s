from prettytable import PrettyTable


def listalldeceased(indi):

    deathPeople = []
    for key, value in indi.items():
        if value.death[0] not in ['', 'N', 'N/A']:

            deathPeople.append(value)
        else:
            continue

    return deathPeople




def listlivemarried(fam):

    livemarried=set()

    for key,value in fam.items():

        husband = value.husband[0]
        wife = value.wife[0]

        if husband.death[0] in ['', 'N', 'N/A']:

            livemarried.add(husband)

        if wife.death[0] in ['', 'N', 'N/A']:

            livemarried.add(wife)

        else:
            continue

    return livemarried


def US2930_prettytable(indi,fam):
    """
    print all list living single person information in a prettytable
    """
    us29=listalldeceased(indi)
    if us29 == []:
        next
    else:
        us29_prettytable = PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death', 'Child', 'Spouse', 'Age'])
        print("US29:List all deceased individuals in a GEDCOM file")
        for value in us29:
             us29_prettytable.add_row([value.indi_id[0], value.name[0],
                                    "Male" if value.gender[0] == "M" else "Female", value.birthday[0],
                                    value.alive, value.death[0], [c[0] for c in value.child]
                                    if value.child != "N/A" else value.child, [c[0] for c in value.spouse]
                                    if value.spouse != "N/A" else value.spouse, value.age])
        print(us29_prettytable)

    us30 = listlivemarried(fam)
    if us30 == {}:
        next
    else:
        us30_prettytable = PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death', 'Child', 'Spouse', 'Age'])
        print("US30:List all living married people in a GEDCOM file")
        for value in us30:
            us30_prettytable.add_row([value.indi_id[0], value.name[0],
                             "Male" if value.gender[0] == "M" else "Female", value.birthday[0],
                            value.alive, "N/A", [c[0] for c in value.child]
                            if value.child != "N/A" else value.child, [c[0] for c in value.spouse], value.age])
        print(us30_prettytable)

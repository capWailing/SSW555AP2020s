from gedcom_app.errors.gedcom_error import GedcomError


def corrent_gender_us21(fam):

    for key, family in fam.items():

        husband = family.husband[0]
        wife = family.wife[0]

        if husband.gender[0] == 'F':
            new_error = GedcomError(("ANOMALY", "FAMILY", "US21", family.husband[1], key),
                                    f"husband's gender should be female")
            family.error_list = new_error

        if wife.gender[0] == 'M':
            new_error = GedcomError(("ANOMALY", "FAMILY", "US21", family.wife[1], key),
                                    f"wife's gender should be male")
            family.error_list = new_error


def unique_family_24(fam):
    person = dict()

    for key, family in fam.items():
        wife = family.wife[0].indi_id[0]

        husband = family.husband[0].indi_id[0]

        if wife in person.keys():

            marry_date = family.married[0]

            if marry_date in person[wife]:
                new_error = GedcomError(("ANOMALY", "FAMILY", "US24", family.married[1], key),
                                        f"wife should have same marry date in different family")
                family.error_list = new_error
            else:
                person[wife].append(marry_date)

        else:
            person[wife] = [family.married[0]]

        if husband in person.keys():

            marry_date = family.married[0]

            if marry_date in person[husband]:
                new_error = GedcomError(("ANOMALY", "FAMILY", "US24", family.married[1], key),
                                        f"husband should have same marry date in different family")
                family.error_list = new_error
            else:
                person[husband].append(marry_date)

        else:
            person[husband] = [family.married[0]]





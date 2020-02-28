if __name__ == "__main__":
    """
    main() function: input path, print two tables
    if data lost, it will view '' in table
    if no record of items, it will view'N/A'
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

        for key, value in indi.items():
            if value['DEAT'] == 'N/A':
                alive = 'TRUE'
            else:
                if value['DATE'] not in ['', 'N/A']:
                    alive = 'FALSE'
                else:
                    alive = 'FALSE'
                    value['DATE'] = ''

            table_indi.add_row([key, value['NAME'], value['SEX'], value['BIRTH'],
                                alive, value['DATE'], value['FAMC'], value['FAMS']])

        for key, value in fam.items():
            id_h = value['HUSB']
            id_w = value['WIFE']
            """ husband id and wife id """
            if id_h not in ['N/A', '']:
                name_h = indi[id_h]['NAME']
            else:
                name_h = 'N/A'
            """ get husband's name"""
            if id_w not in ['N/A', '']:
                name_w = indi[id_w]['NAME']
            else:
                name_w = 'N/A'
            """ get wife's name"""

            if value['DIV'] == 'N/A':
                value['DATE'] = 'N/A'
            elif value['DATE'] in ['', 'N/A']:
                value['DATE'] = ''
            """
            if div record lost, print''
            if no divorce, print'N/A'
            """
            table_fam.add_row([key, value['MARR'], value['DATE'],
                               id_h, name_h, id_w, name_w, value['CHIL']])

        print(table_indi)
        print(table_fam)
"""
    author: Zituo Yan
    description: Start application
    date:21/02/2020
"""

from gedcom_app.control.parser import parse_gedcom
from gedcom_app.view.output_errors import output_errors_indi, output_errors_fam
from gedcom_app.view.output_prettytable import individual_table, family_table
from gedcom_app.control.build_entity import build_individual, build_family
from gedcom_app.control.verification import verification


def main():
    path = ""
    while len(path) == 0:
        path = input("Please enter your GEDCOM file path:\n")

    dict_indi, dict_fam = parse_gedcom(path)
    indi_list = build_individual(dict_indi)
    fam_list = build_family(dict_fam, indi_list)
    individual_table(indi_list)
    family_table(fam_list)
    verification(indi_list, fam_list)
    output_errors_indi(indi_list)
    output_errors_fam(fam_list)


if __name__ == '__main__':
    main()

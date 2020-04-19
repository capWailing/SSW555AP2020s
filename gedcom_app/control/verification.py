"""
    author: Zituo Yan
    description: this starts the verification part
    date: 3/2/2020
"""
from gedcom_app.control.US15 import multiple_siblings
from gedcom_app.control.US38 import list_recent_birth_prettytable
from gedcom_app.control.child_birth import birth_before_marriage
from gedcom_app.control.us07 import less_than_150
from gedcom_app.control.us14 import multiple_birth
from gedcom_app.control.US0203 import birth_b_marriage_us02, birth_b_death_us03
from gedcom_app.control.US1217 import parents_not_too_old_us12, no_marriage_to_children_us17
from gedcom_app.control.sibi_not_marry import sibi_not_marry
from gedcom_app.control.marr_after_14 import marry_after_14
from gedcom_app.control.us0106 import date_before_current, div_before_death
from gedcom_app.control.US0405 import USO4, US05
from gedcom_app.control.US11 import US11
from gedcom_app.control.US2527 import unique_first_names_in_families_us25
from gedcom_app.control.US2124 import corrent_gender_us21, unique_family_24
from gedcom_app.control.US1923 import unique_name_and_birthday_us23, first_cousin_should_not_marry_us19
from gedcom_app.control.US31 import list_living_single_us31_prettytable
from gedcom_app.control.US32 import list_multiple_birth_us32_prettytable
from gedcom_app.control.US3536 import pretty_table_recent_births, pretty_table_recent_death
from gedcom_app.control.US2930 import US2930_prettytable


def verification(indi_dict, fam_dict):
    birth_before_marriage(fam_dict)
    less_than_150(indi_dict)
    multiple_birth(fam_dict)
    birth_before_marriage(fam_dict)
    birth_b_marriage_us02(fam_dict)
    birth_b_death_us03(indi_dict)
    parents_not_too_old_us12(fam_dict)
    no_marriage_to_children_us17(fam_dict)
    sibi_not_marry(fam_dict)
    marry_after_14(fam_dict)
    date_before_current(indi_dict, fam_dict)
    div_before_death(fam_dict)
    USO4(fam_dict)
    US05(fam_dict)
    US11(indi_dict, fam_dict)
    corrent_gender_us21(fam_dict)
    unique_family_24(fam_dict)
    multiple_siblings(fam_dict)
    unique_first_names_in_families_us25(fam_dict)
    unique_name_and_birthday_us23(indi_dict)
    first_cousin_should_not_marry_us19(fam_dict)
    list_living_single_us31_prettytable(indi_dict)
    list_multiple_birth_us32_prettytable(indi_dict, fam_dict)
    US2930_prettytable(indi_dict, fam_dict)
    pretty_table_recent_births(indi_dict)
    pretty_table_recent_death(indi_dict)
    list_recent_birth_prettytable(indi_dict)


from unittest import TestCase
from gedcom_app.control.US2930 import listalldeceased,listlivemarried
from gedcom_app.tests.build_instance import build_family_list,build_individual_list


class TestUS2127(TestCase):

    def test_listalldeceased(self):
        path = r"..\..\test2930.ged"
        individual_list=build_individual_list(path)
        deathpeople=listalldeceased(individual_list)
        list1=[[i.indi_id[0]] for i in deathpeople]

        self.assertEqual(list1,
                         [['I0291']])

    def test_listlivemarried(self):
        path = r"..\..\test2930.ged"
        indi_dict = build_individual_list(path)
        livemarried=listlivemarried(indi_dict)
        list2=[[i.indi_id[0]] for i in livemarried]
        list2.sort()
        self.assertEqual(list2,[['I0292'],['I0293'],['I0294'],['I0295']])
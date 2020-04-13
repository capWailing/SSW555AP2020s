from unittest import TestCase
from gedcom_app.control.US2930 import listalldeceased,listlivemarried
from gedcom_app.tests.build_instance import build_family_list,build_individual_list


class TestUS2127(TestCase):

    def test_listalldeceased(self):
        path = r"..\..\test2930.ged"
        individual_list=build_individual_list(path)
        list1=listalldeceased(individual_list)

        self.assertEqual(list1,
                         ["US29:ID:I0291; Name:Qi /kang/; Gender:M; Birthday:9 JUL 1950; Death31 DEC 1980; Famc:['N/A']; Fams:['F1291']"])

    def test_listlivemarried(self):
        path = r"..\..\test2930.ged"
        family_dict = build_family_list(path)
        list2=listlivemarried(family_dict)

        self.assertEqual(list2,
                         {"US30:ID:I0292; Name:Xiao /Wu/; Gender:F; Birthday:28 SEP 1950; Death:N/A; Famc:['N/A']; Fams:['F1291']",
                          "US30:ID:I0295; Name:Xiang /Li/; Gender:M; Birthday:9 SEP 1954; Death:N/A; Famc:['N/A']; Fams:['F1293']",
                          "US30:ID:I0293; Name: Liu /Kang/; Gender:M; Birthday:15 JUL 1955; Death:N/A; Famc:['N/A']; Fams:['F1292']",
                          "US30:ID:I0294; Name:Cao /Meng/; Gender:F; Birthday:4 SEP 1957; Death:N/A; Famc:['N/A']; Fams:['F1292', 'F1293']"})
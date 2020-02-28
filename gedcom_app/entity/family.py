"""
    author: Zituo Yan
    description: class for family entity
    date: 27/02/2020
"""


class Family:
    """
        This is a class for describe family
    """

    def __init__(self, fam_id, married, divorced, husband, wife, children):
        """
            init family class
        :param fam_id: family id
        :param married: married date
        :param divorced: divorced date or N/A if not divorced
        :param husband: husband instance from class indi
        :param wife: wife instance from class indi
        :param children: children individual id list
        """
        self.__id = fam_id
        self.__married = married
        self.__divorced = divorced
        self.__husband = husband
        self.__wife = wife
        self.__children = children
        self.__error_list = []

    @property
    def id(self):
        """
            get family id
        :return: family id
        """
        return self.__id

    @property
    def married(self):
        """
            get married date
        :return: married date
        """
        return self.__married

    @property
    def divorced(self):
        """
            get divorced date or N/A
        :return: divorced date or N/A
        """
        return self.__divorced

    @property
    def husband(self):
        """
            get husband instance from class indi
        :return: husband instance
        """
        return self.__husband

    @property
    def wife(self):
        """
            get wife instance from class indi
        :return: wife instance
        """
        return self.__wife

    @property
    def children(self):
        """
            get children list with children id
        :return: list of children id
        """
        return self.__children

    @property
    def error_list(self):
        """
            listed errors which are gedcom-errors
        :return: list of errors
        """
        return self.__error_list

    @error_list.setter
    def error_list(self, error_list):
        """
            set error list
        :param error_list:
        :return:
        """
        self.__error_list = error_list

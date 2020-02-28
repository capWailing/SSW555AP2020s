"""
    author: Zituo Yan
    description: class for individuals
    date: 28/02/2020
"""


class Individual:
    """
        individual entity class
    """
    def __init__(self, indi_id, name, gender, birthday, death, child, spouse):
        """
            init individual instance
        :param indi_id: individual id
        :param name: individual name
        :param gender: individual gender
        :param birthday: birthday
        :param death: death date
        :param child: individual instance of child
        :param spouse: list of individual instance of spouse
        """
        self.__indi_id = indi_id
        self.__name = name
        self.__gender = gender
        self.__birthday = birthday
        self.__death = death
        self.__child = child
        self.__spouse = spouse
        self.__alive = True
        self.__error_list = []

    @property
    def indi_id(self):
        """
            individual id
        :return: id
        """
        return self.__indi_id

    @property
    def name(self):
        """
            individual name
        :return: name
        """
        return self.__name

    @property
    def gender(self):
        """
            individual gender
        :return: gender
        """
        return self.__gender

    @property
    def birthday(self):
        """
            individual birth date
        :return: birthday
        """
        return self.__birthday

    @property
    def death(self):
        """
            individual death date
        :return: death date
        """
        return self.__death

    @property
    def child(self):
        """
            instance of individual class which is child of this
        :return: child
        """
        return self.__child

    @property
    def spouse(self):
        """
            a list of instance of individual class which is spouse of this
        :return:
        """
        return self.__spouse

    @property
    def alive(self):
        """
            whether the individual is alive, default True
        :return: alive
        """
        return self.__alive

    @alive.setter
    def alive(self, alive):
        """
            set the individual is alive or not
        :param alive: True or False
        :return:
        """
        self.__alive = alive

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

"""
    author: Zituo Yan
    description: this is a class of errors of GEDCOM file
    date: 28/02/2020
"""


class GedcomError:
    """
        this is a class of errors occur in the GEDCOM file
    """
    def __init__(self, error_info, error_message):
        """
            init GEDCOM error instance
        :param error_info: this is a tuple of information of error which should include
                            the following column
            error_type:  'ERROR' or 'ANOMALY' this is the start of error report
            indi_or_fam:  'INDIVIDUAL' or 'FAMILY' this should be error from individual or family
            user_story:  'US01' for example. this is the user story number
            error_line:  the number of line in the GEDCOM file
            entity_id:  this should be the id of individual or family
        :param error_message: this is a string type of message that identifies what's wrong
            'Birthday 2020-01-01 occurs in the future' for example
        """
        self.__error_info = error_info
        self.__error_message = error_message

    @property
    def error_info(self):
        """
            return a dictionary that records error information from error_info
        :return: dictionary
        """
        return {"error_type": self.__error_info[0],
                "indi_or_fam": self.__error_info[1],
                "user_story": self.__error_info[2],
                "error_line": self.__error_info[3],
                "entity_id": self.__error_info[4]}

    @property
    def error_message(self):
        """
            return the message from error_message
        :return: error_message
        """
        return self.__error_message

    def __str__(self):
        return f"{self.error_info['error_type']}: {self.error_info['indi_or_fam']}: \
{self.error_info['user_story']}: {self.error_info['error_line']}: \
{self.error_info['entity_id']}: {self.error_message}"

    def __eq__(self, other):
        if isinstance(other, str):
            return True if self.__str__ == other else False
        shared_items = {k: self.error_info[k] for k in self.error_info
                        if k in other.error_info and self.error_info[k] == other.error_info[k]}
        return True if shared_items == 5 and self.error_message == other.error_info else False

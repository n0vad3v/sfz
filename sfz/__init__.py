from sfz.code import *

__author__ = 'Nova Kwok <n0vad3v@riseup.net>'
name = "sfz"

class Sfz:
    def __init__(self,number):
        self.number = number
        self.year = int(self.number[6:10])
        self.month = int(self.number[10:12])
        self.day = int(self.number[12:14])
        self.loc_code = self.number[0:6]

    def gender(self):
        chk = int(self.number[16:17])
        if chk %2 == 0:
            return "女"
        else:
            return "男"

    def loc(self):
        """
        Takes the first 6 digits to determine the location of the specified ID card.
        :return: string or "Unknown" if not in code_list
        """
        code = self.loc_code
        if code in code_list:
            return code_list[code]
        else:
            return "Unknown"


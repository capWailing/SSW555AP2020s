"""
    author: Zituo Yan
    description: verify the valid tags in GEDCOM file
    date: 07/02/20
"""


def open_file(path):
    try:
        rf = open(path, 'r', encoding='utf8')
    except FileNotFoundError:
        print(f"File not found: {path}")
    else:
        with rf:
            return rf.readlines()


class VerifyTags:
    valid_tags = {"level0": ["HEAD", "NOTE", "TRLR"],
                  "level0id": ["INDI", "FAM"],
                  "level1INDI": ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS"],
                  "level1FAM": ["MARR", "HUSB", "WIFE", "CHIL", "DIV"],
                  "level2": ["DATE"],
                  "level2valid": ["BIRT", "DEAT", "MARR", "DIV"]}

    def __init__(self, path):
        file_list = open_file(path)
        self.file = []
        for line in file_list:
            current_list = line.strip("\n").split(maxsplit=2)
            if len(current_list) == 2:
                current_list.append(" ")
            self.file.append(current_list)

    def verify_tags(self):
        for offset, line in enumerate(self.file):
            print("--> " + " ".join(line))
            if line[0] == "0":
                self.verify_level_0(line)
            elif line[0] == "1":
                self.verify_level_1(line, offset)
            elif line[0] == "2":
                self.verify_level_2(line, offset)
            else:
                self.__print_false(line)

    def verify_level_0(self, line):
        if line[1] in self.valid_tags.get("level0"):
            self.__print_true(line)
        elif line[2] in self.valid_tags.get("level0id"):
            current_line = line.copy()
            a = current_line[1]
            current_line[1] = current_line[2]
            current_line[2] = a
            self.__print_true(current_line)
        elif line[1] in self.valid_tags.get("level0id"):
            self.__print_false(line)
        else:
            self.__print_false(line)

    def verify_level_1(self, line, offset):
        if offset == 0:
            self.__print_false(line)
        elif line[1] in self.valid_tags.get("level1INDI"):
            for i in range(offset - 1, 0, -1):
                if self.file[i][0] == "0":
                    if self.file[i][2] == "INDI":
                        self.__print_true(line)
                        return
            self.__print_false(line)
        elif line[1] in self.valid_tags.get("level1FAM"):
            for i in range(offset - 1, 0, -1):
                if self.file[i][0] == "0":
                    if self.file[i][2] == "FAM":
                        self.__print_true(line)
                        return
            self.__print_false(line)
        else:
            self.__print_false(line)

    def verify_level_2(self, line, offset):
        if offset < 2:
            self.__print_false(line)
        elif line[1] in self.valid_tags.get("level2"):
            if self.file[offset - 1][0] == "1":
                if self.file[offset - 1][1] in self.valid_tags.get("level2valid"):
                    self.__print_true(line)
                    return
                else:
                    self.__print_false(line)
                    return
        self.__print_false(line)

    @staticmethod
    def __print_true(line):
        current_line = line.copy()
        current_line.insert(2, "Y")
        print("<-- " + "|".join(current_line))

    @staticmethod
    def __print_false(line):
        current_line = line.copy()
        current_line.insert(2, "N")
        print("<-- " + "|".join(current_line))


def main():
    path = ""
    while len(path) == 0:
        path = input("Enter file name:\n")
    tag = VerifyTags(path)
    tag.verify_tags()


if __name__ == '__main__':
    main()

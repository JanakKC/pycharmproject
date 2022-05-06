class Human:
    def __init__(self, x, y):
        self.name = x
        self.surname = y


a1 = Human("RAM", "Poudel")
print(a1.name + " " + a1.surname)


class human:
    def __init__(self, x, y):
        self.__name = x
        self.__surname = y

    def print(self):
        print(self.__name)
        print(self.__surname)

    def getabc(self):
        return (self.__name)

a1=human("ram","poudel")
print(a1.getabc)
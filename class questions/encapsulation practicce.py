class Human:
    def __init__(self, x, y):
        self.__name = x
        self.__city = y

    def a(self):
        print(self.__name)
        print(self.__city)
        print(self.__name+ " " + "lives" + " " + "in " + self.__city)


h1 = Human("ram", "ktm")
h1.a()


class Human:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


h1 = Human()
h1.setName("RONALDO")
print(h1.getName())

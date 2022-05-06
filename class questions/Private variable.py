class Human:
    def __init__(self, x, y):
        self.name = x
        self.__city = y

    def a(self):
        print(self.__city)


a1 = Human("ram", "KTM")
print(a1.name)
a1.a()


class School:
    def __init__(self, x, y):
        self.__name = x
        self.__no_of_students = y

    def a(self):
        print(self.__name)
        print(self.__no_of_students)


c1 = School("Royal", 500)
c1.a()

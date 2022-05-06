class human:
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city

    def a(self):
        print(self.__name)
        print(self.__age)
        print(self.__city)


a1 = human("HARI", 19, "PKH")
a1.a()

class Human:
    def __init__(self, x, y):
        self.name = x


h1 = Human("ram", "ktm")
print(h1.name)


class Human:
    def __init__(self, x, y):
        self.name = x  # it is a public variable
        self.__city = y
        """private variable cannot be acess outdide the class but can be access anywhere
           within the class"""


h1 = Human("ram", "ktm")
print(h1.name)
print(h1.__city)



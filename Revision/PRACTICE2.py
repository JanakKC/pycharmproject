class Human:
    def __init__(self, name, city, age, email):
        self.__name = name
        self.__city = city
        self.__age = age
        self.__email = email

    def getName(self):
        return self.__name

    def getCity(self):
        return self.__city


h1 = Human("SHYAM", "KTM", 22, "shyam@gmail.com")
# h1 is instantiated and private properties are initialized through constructor.
a = h1.getName()
print(a)

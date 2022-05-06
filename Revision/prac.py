class Human:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setCity(self, city):
        self.__city = city

    def getCity(self):
        return self.__city

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email


h1 = Human()
h1.setName("HARI")
h1.setCity("PKH")
h1.setAge(19)
h1.setEmail("hari@gmail.com")
print(h1.getName())
print(h1.getCity())
print(h1.getAge())
print(h1.getEmail())
print()





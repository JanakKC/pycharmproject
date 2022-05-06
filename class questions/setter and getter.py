"""
encapsulation is a process of making all instance variable private and accessing them through public function.
"""


class Human:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setCity(self, city):
        self.__city = city

    def getCity(self):
        return self.__city


h1 = Human()
h1.setName("ram")
h1.setCity("ktm")
print(h1.getName() + " Lives in " + h1.getCity())
h2 = Human()
h2.setName("rabi")
h2.setCity("pkh")

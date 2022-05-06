class Employee:
    def __init__(self):
        self.__name = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary


a1 = Employee()
a1.setName("Janak")
a1.setSalary("10000")
print(a1.getName() + " " + "receives salary of" + " " + a1.getSalary())

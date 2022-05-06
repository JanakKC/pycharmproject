'''
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
class countries:
    def __init__(self):
        print("abc")
        print("xyz")


class nepal(countries):
    def __init__(self):
        super() .__init__()
        print(123)


class india(countries):
    def war(self):
        print("MMM")


class China(countries):
    def __init__(self):
        super().__init__()
        print("JJJ")


a1 = China()
a2 = nepal()
a3 = india()
a3.war()

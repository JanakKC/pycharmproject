#To create a class, use the keyword class:
class human():
    x="apple"
    print(x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class machine:
    def output(self):
        print("students")
    def website(self):
        print("facebook")


computer = machine()
computer.output()
computer.website()

class human:
    def __init__(self):  # constructor function
        print("hello")

    def walk(self):
        print("hi")


a1 = human()
a1.walk()
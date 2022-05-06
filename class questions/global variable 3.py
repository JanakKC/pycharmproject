class Human:
    no_of_hands = "two hands"  # class variable is shared by all instances of a class

    def __init__(self, firstname, lastname):
        self.name = firstname + " " + lastname  # instance variable value is only accessed by the same instance

    def properties(self):
        print(self.name + " has " + self.no_of_hands)


h1 = Human("ram", "sharma")
h1.properties()
h2 = Human("hari", "shrestha")
h2.properties()
print(h1.no_of_hands)
print(h2.no_of_hands)
print(h1.name)
print(h2.name)
34r

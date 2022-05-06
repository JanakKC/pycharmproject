class Human:
    def __init__(self, x, y):
        self.name = x
        self.city = y

    def walk(self):
        print("Human can walk")


class Male(Human):
    def __init__(self):
        super().__init__("ram", "ktm")
        print("male can walk")

    def walk(self):
        print("i can walk")


objMale = Male()
objMale.walk()
a1 = Human("x", "y")
a1.walk()

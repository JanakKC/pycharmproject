class Human:
    def __init__(self, x, y):
        self.name = x
        self.city = y

    def walk(self):
        print("Human can walk")


class Male(Human):
    def walk(self):
        super().__init__("X", "Y")
        print("male can walk")
        super().walk()


objMale = Male("J", "k")
objMale.walk()

class Human:
    def __init__(self, x, y):
        self.name = x
        self.city = y

    def walk(self):
        print("Human can walk")  # class varibale and onject variable


class Male(Human):
    def __init__(self):
        super().__init__()
        print("male can walk")
        super().walk()

    def walk(self):
        print("male can walk")




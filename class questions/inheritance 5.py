class Human:
    def __init__(self):
        print("asian")


class Male(Human):
    def __init__(self):
        super().__init__()
        print("indian")


class Son(Male):
    pass
class Daughter(Human):
    def __init__(self):
        super().__init__()
        print("chinese")


a1 = Daughter()

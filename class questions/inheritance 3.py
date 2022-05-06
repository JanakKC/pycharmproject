class human:
    def __init__(self) -> object:
        print("this is parent class constructor")

    def talk(self):
        print("hello")


class male(human):
    def __init__(self):
        super() .__init__();
        print("this is child class constructor")

class female(human):
    def talk(self):
        print("bie")
m1=male()

"""object create huda constructor function call hunxa
aafnai constructor function xaena bhane parent ko constructor function run hunxa"""


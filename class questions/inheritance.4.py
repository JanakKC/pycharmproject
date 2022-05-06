class human:
    def __init__(self):
        print("this is parent class constructor")

    def talk(self):
        print("hello")


class male(human):
    def __init__(self):
        super().__init__()
        print("this is child class constructor")


class female(human):
    def talk(self):
        print("bie")


m1 = male()


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

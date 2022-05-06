class human:
    def walk(self):
        print("Hi")

    def talk(self):
        print("hello")


class male(human):
    pass


class female(human):
    def talk(self):
        print("bie")


m1 = male()
m1.talk()
f1 = female()
f1.talk()
f1.walk()

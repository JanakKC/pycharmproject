class human:
    def walk(self):
        print("hi")

    def talk(self):
        print("hello")


class male(human):
    pass


m1 = male()
m1.walk()
m1.talk()


class school:
    def read(self):
        print("students")

    def write(self):
        print(1)


class college(school):
    pass


c1 = college()
c1.read()
c1.write()

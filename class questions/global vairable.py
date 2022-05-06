class a:
    def a1(self):
        global x
        x = 2
        print(x)

    def a2(self):
        print(x)


obja = a()
obja.a1()
obja.a2()


class b:
    def x(self):
        global y
        y = 2
        print(x)

    def b(self):
        print(y)


objb = b()
objb.x()

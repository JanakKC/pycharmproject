class a:
    x = 5

    def a1(self):
        global x
        x = 2
        print(x)

    def a2(self):
        print(self.x)


obja = a()
obja.a1()
obja.a2()

class Sports:
    country = "nepal"

    def __init__(self, club, city):
        self.name = club + " " + city

    def properties(self):
        print(self.name + " " "from" + " " + self.country)


a1 = Sports("kapanfc", "ktm")
a1.properties()  # access modifier

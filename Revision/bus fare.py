class vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(vehicle):
    pass

    def fare(self):
        bus_fare = self.capacity * 100
        total_fare = bus_fare + ((10/100) * bus_fare)
        return total_fare


a1 = vehicle("Everest", 50)
print("total fare is", a1.fare())

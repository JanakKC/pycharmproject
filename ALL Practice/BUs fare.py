class Vehicle:
    def __init__(self, name,  capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):

    def fare(self):
        fare_car = self.capacity * 100
        total_fare = fare_car + (0.1 * fare_car)
        return total_fare




School_bus = Bus("Everest ", 50)
print("Total Bus fare is:", School_bus.fare())


a = 33
b = 200

if b > a:
  pass

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

for x in range(6):
  print(x)

for x in range(2, 30, 3):
  print(x)
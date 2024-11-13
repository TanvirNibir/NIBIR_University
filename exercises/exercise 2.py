class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")
    print(f"{self.brand}, {self.model}")

class Boat(Car):
  def __init__(self, brand, model):
      super().__init__(brand, model)

  def move(self):
    print("Sail!")
    print(self.brand)
    print(self.model)

class Plane(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)


    def move(self):
      print("Fly!")
      print(f"{self.brand}, {self.model}")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class
plane2 = Plane("Hulo", "435")
for x in (car1, boat1, plane1, plane2):
  x.move()
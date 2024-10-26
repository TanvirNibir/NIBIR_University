class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def print_properties(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")

    def accelerate(self, change_speed):
        self.current_speed += change_speed

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self,hours):
        self.travelled_distance += self.current_speed * hours

    def print_current_speed(self):
        print(f"Current Speed: {self.current_speed} km/h")

car = Car("ABC-123", 200)

# Accelerate
car.accelerate(70)
car.print_current_speed()

# Drive the car for 1.5 hours
car.drive(1.5)
car.print_properties()

# Drive the car for another 2 hours, because the car has already travelled for 1.5 hrs (90 + 60 * 2)
car.drive(2)
car.print_properties()
#3
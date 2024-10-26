import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.traveled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed = max(0, min(self.current_speed + speed_change, self.max_speed))

    def drive(self, hours):
        self.traveled_distance += self.current_speed * hours


cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

race_finished = False
while not race_finished:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

    # After all cars have driven for 1 hour, check if any car has reached 10,000 km
    race_finished = any(car.traveled_distance >= 10000 for car in cars)

print(f"{'Registration':<15}{'Max Speed':<15}{'Current Speed':<15}{'Traveled Distance'}")
print("=" * 60)
for car in cars:
    print(f"{car.registration_number:<15}{car.max_speed:<15}{car.current_speed:<15}{round(car.traveled_distance, 2)}")

winners = [car for car in cars if car.traveled_distance >= 10000]
if winners:
    print("\nWinner(s):")
    for winner in winners:
        print(f"{winner.registration_number} with {round(winner.traveled_distance, 2)} km traveled!")
#4
# Exercise 4

import random

class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.trav_dist = 0

    def accelerate(self):
        speed_change = random.randint(-10, 15)
        new_speed = self.current_speed + speed_change
        self.current_speed = max(0, min(new_speed, self.max_speed))

    def drive(self):
        self.trav_dist += self.current_speed

    def __str__(self):
        return f"{self.reg_number:>12} | {self.max_speed:>10} km/h | {self.current_speed:>13} km/h | {self.trav_dist:>15} km"


class Race:
    def __init__(self, name, distance, car):
        self.name = name
        self.distance = distance
        self.car = car

    def hour_passes(self):
        for car in self.car:
            car.accelerate()
            car.drive()

    def print_status(self):
        print(f"\n{'Registration':>12} | {'Max Speed':>10} | {'Current Speed':>13} | {'Distance Traveled':>15}")
        print("-" * 56)
        for car in self.car:
            print(car)

    def race_finished(self):
        return any(car.trav_dist >= self.distance for car in self.car)


if __name__ == "__main__":

    cars = []
    for i in range(1, 11):
        reg_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        car = Car(reg_number, max_speed)
        cars.append(car)


    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1

        if hours % 10 == 0:
            print(f"\nStatus after {hours} hours:")
            race.print_status()

    print(f"\nRace completed in {hours} hours!")
    race.print_status()

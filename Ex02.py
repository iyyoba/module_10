# Exercise 2
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def move_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved to floor {self.current_floor}")
        else:
            print("Elevator is already at the top floor.")

    def move_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved to floor {self.current_floor}")
        else:
            print("Elevator is already at the bottom floor.")

    def go_to_floor(self, floor):
        if self.bottom_floor <= floor <= self.top_floor:
            print(f"Elevator moving from floor {self.current_floor} to floor {floor}.")
            while self.current_floor < floor:
                self.move_up()
            while self.current_floor > floor:
                self.move_down()
            print(f"Elevator has arrived at floor {self.current_floor}.")
        else:
            print("Invalid Floor")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Running elevator {elevator_number} to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid Floor.")

if __name__ == "__main__":

    my_building = Building(1, 10, 3)


    my_building.run_elevator(0, 5)  # Elevator 0 goes to floor 5
    my_building.run_elevator(1, 7)  # Elevator 1 goes to floor 7
    my_building.run_elevator(2, 3)  # Elevator 2 goes to floor 3
    my_building.run_elevator(0, 1)  # Elevator 0 goes to floor 1

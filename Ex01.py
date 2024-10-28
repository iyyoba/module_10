# Exercise 1
class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Moving up... now on floor {self.current_floor}")
        else:
            print("Already at the top floor!")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Moving down... now on floor {self.current_floor}")
        else:
            print("Already at the bottom floor!")

    def go_to_floor(self, target_floor: int):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print("Invalid floor!")
            return

        print(f"Start at: {self.current_floor}")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}")



if __name__ == "__main__":
    elevator = Elevator(0, 10)

    print("Moving to floor 5:")
    elevator.go_to_floor(3)

    print("\nReturning to the bottom floor:")
    elevator.go_to_floor(0)

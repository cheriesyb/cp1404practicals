from prac_06.car import Car

"""car = Car("Buik", 100)
car.add_fuel(150)
car.drive(200)
print(car)"""


def main():
    get_car_name = input("Enter your car name: ")
    car = Car(get_car_name)
    print(car)

    print("d) drive\nr) refuel\nq) quit")
    user_choice = input("Enter your choice: ")
    while user_choice != "q":
        if user_choice == "d":
            pass
        elif user_choice == "r":
            pass
        else:
            print("Invalid choice")


main()
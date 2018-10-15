from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "C":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            chosen_taxi = taxis[taxi_choice]
        elif user_choice == "D":
            chosen_taxi.start_fare()
            drive_how_much = float(input("Drive how far? "))
            chosen_taxi.drive(drive_how_much)
            trip_cost = chosen_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(chosen_taxi.name, trip_cost))
            total_bill += trip_cost
        else:
            print("Invalid menu choice")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        user_choice = input(">>> ").upper()
    print("Total trip cost: {:.2f}".format(total_bill))
    print("Taxis are now: ")
    display_taxis(taxis)



def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))




main()
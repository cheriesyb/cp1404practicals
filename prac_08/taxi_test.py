from prac_08.taxi import Taxi

def main():
    prius = Taxi("Prius 1", 100, 1.23)
    print(prius)
    prius.drive(40)
    print(prius)
    prius.start_fare()
    print(prius)
    prius.drive(100)
    print(prius)


main()
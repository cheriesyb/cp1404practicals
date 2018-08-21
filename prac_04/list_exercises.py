numbers = []

def main():
    for number in range(5):
        value = input("Number: ")
        numbers.append(value)

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[4]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format()) #find the average

main()



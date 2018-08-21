MIN_LENGTH = 4


def main():
    password = validate_password(MIN_LENGTH)
    print_stars(password)


def validate_password(min_length):
    password = input("Please enter password (min. {}): ".format(MIN_LENGTH))
    while len(password) < min_length:
        password = input("Enter password again: ")
    return password


def print_stars(sequence):
    print('*' * len(sequence))


main()
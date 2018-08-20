MIN_LENGTH = 4


def main():
    password = get_password()
    print_stars(password)


def get_password():
    password = validate_password(MIN_LENGTH)
    return password


def validate_password(min_length):
    password = input("Please enter password (min. {}): ".format(MIN_LENGTH))
    while len(password) < min_length:
        password = input("Enter password again: ")
    return password


def password():
    global print_stars

    def print_stars(sequence):
        print('*' * len(sequence))


password()


main()
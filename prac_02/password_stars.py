
def main():

    password = get_password()
    print_asterisk(password)


def print_asterisk(password):
    """A function that print asterisks"""
    print(len(password) * "*")


def get_password():
    """A program that gets the password from the user and checks the valid length"""
    password = input("Enter a password: ")
    while len(password) < 6:
        print("Your password must be at least 5 characters long!")
        password = input("Enter a password: ")
    return password


main()
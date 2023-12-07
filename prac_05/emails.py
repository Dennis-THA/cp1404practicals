
def main():
    """Dictionary of email and names"""
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n)").upper()
        if confirmation != 'Y' and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    """Extract name from the email address"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
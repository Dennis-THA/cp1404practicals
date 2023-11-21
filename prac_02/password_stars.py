
password = input("Enter a password: ")
while len(password) < 6:
    print("Your password must be at least 5 characters long")
    password = input("Enter a password: ")
print(len(password) * "*")
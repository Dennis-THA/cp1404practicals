
MENU = "(G)et score\n(P)rint\n(S)how\n(Q)uit"


def main():
    score = 0
    print(MENU)
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            display_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter choice: ").upper()
    print("Farewell")


def display_stars(score):
    """This function is to display stars based on score."""
    for i in range(score):
        print('*', end='')
    print()


def determine_result(score):
    """This function is to determine the result based on the score."""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def validate_score():
    """This is a function to get a valid score"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


main()

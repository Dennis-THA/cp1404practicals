
MENU = "(G)et score\n(P)rint\n(S)how\n(Q)uit"


def main():
    print(MENU)
    score = 0
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


def display_stars(score):
    for i in range(score):
        print('*', end="")


def determine_result(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def validate_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


main()

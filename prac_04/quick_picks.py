
import random

MAX_NUMBER_PER_LINE = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    """This program generates quick pick lines based on the input """
    number_of_quick_picks = get_quick_picks()
    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(MAX_NUMBER_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))


def get_quick_picks():
    """This function makes sure the number of quick picks is valid"""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("The number of quick picks must be at least 1!")
        number_of_quick_picks = int(input("How many quick picks? "))
    return number_of_quick_picks


main()

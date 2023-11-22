
import random
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(f"Random score is {random_score}")
    random_result = determine_result(random_score)
    print(result)
    print(random_result)


def determine_result(score):
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
import levels as lvl


LEVELS = [1, 2]

LEVEL_DIGITS = {1: "simple operations with numbers 2-9",
                2: "integral squares of 11-29"}


def saving_the_result(name: str, correct_answers: int, level: int) -> None:
    """
    Writes the user's name and the number of correct answers indicating the difficulty level to the file
    :param name: username
    :param correct_answers: the number of correctly solved examples by the user
    :param level: the level of complexity of the examples
    """
    with open("results.txt", "a") as file:
        if level in LEVELS:
            file.write(f"{name}: {correct_answers}/5 in level {level} ({LEVEL_DIGITS[level]}).\n")


def main() -> None:
    correct_answers = 0

    while True:
        print("Which level do you want? Enter a number:")

        for key in LEVEL_DIGITS:
            print(f"{key} - {LEVEL_DIGITS[key]}")

        level = lvl.checking_the_integer_value()

        if level == LEVELS[0]:
            correct_answers = lvl.simple_level(correct_answers)
            break
        elif level == LEVELS[1]:
            correct_answers = lvl.complex_level(correct_answers)
            break
        else:
            print("Incorrect format.")

    print(f"Your mark is {correct_answers}/5.")
    permission = input("Would you like to save your result to the file? Enter yes or no. ")

    if permission.lower() in ["yes", "y"]:
        name = input("What is your name? ")
        saving_the_result(name, correct_answers, level)
        print('The results are saved in "results.txt".')


if __name__ == "__main__":
    lvl.seed()
    main()

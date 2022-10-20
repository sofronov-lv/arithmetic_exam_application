def checking_the_integer_value() -> int:
    while True:
        try:
            return int(input())
        except ValueError:
            print("Wrong format! Try again.")


def check_the_answer(answer: int) -> int:
    """
    Checks the correctness of the user's response to the created example
    :param answer: the correct answer calculated by the program
    :return: returns 1 or 0 depending on whether the user has solved the example correctly
    """
    while True:
        user_answer = checking_the_integer_value()

        if user_answer == answer:
            print("Right!")
            return 1
        else:
            print("Wrong!")
            return 0

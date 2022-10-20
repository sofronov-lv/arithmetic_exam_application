from random import seed, randint, choice
from checks import checking_the_integer_value, check_the_answer


NUMBER_OF_EXAMPLES = 5


def generating_complex_examples() -> int:
    """
    Generates a pseudo-random example of difficulty level 2
    :return: the correct answer calculated by the program
    """
    start, stop = 11, 29
    a = randint(start, stop)
    b = 2

    example = a ** b
    print(a)

    return example


def generating_simple_examples() -> int:
    """
    Generates a pseudo-random example of difficulty level 1
    :return: the correct answer calculated by the program
    """
    start, stop = 2, 9
    a = randint(start, stop)
    operator = choice("+-*")
    b = randint(start, stop)

    example = f"{a} {operator} {b}"
    print(example)

    return eval(example)


def complex_level(correct_answers: int) -> int:
    """
    Records the sum of the correct answers from NUMBER_OF_EXAMPLES 2 level (integral squares of 11-29)
    :param correct_answers: the initial number of correct answers is zero
    :return: the number of correctly solved examples by the user
    """
    for i in range(NUMBER_OF_EXAMPLES):
        answer = generating_complex_examples()
        correct_answers += check_the_answer(answer)

    return correct_answers


def simple_level(correct_answers: int) -> int:
    """
    Records the sum of the correct answers from NUMBER_OF_EXAMPLES 1 level (simple operations with numbers 2-9)
    :param correct_answers: the initial number of correct answers is zero
    :return: the number of correctly solved examples by the user
    """
    for i in range(NUMBER_OF_EXAMPLES):
        answer = generating_simple_examples()
        correct_answers += check_the_answer(answer)

    return correct_answers

import random


def is_even(number: int) -> str:
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def brain_even_game() -> list:
    stack = []
    stack.append('Answer \"yes\"'
+ ' if the number is even, otherwise answer \"no\".')
    for i in range(1, 4):
        number = random.randint(1, 100)
        stack.append([number, is_even(number)])
    return stack

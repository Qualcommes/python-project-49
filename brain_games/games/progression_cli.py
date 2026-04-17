import random


def get_progression(first: int, step: int, n: int) -> list:
    stack = []
    position = random.randint(1, n)
    number = 0
    progression = ''
    for i in range(1, n + 1):
        if i == position:
            progression += '.. '
            number += first
            first += step
            continue
        progression += str(first) + ' '
        first += step
    stack += [progression, number]
    return stack


def brain_progression_game() -> list:
    stack = []
    stack.append('Whut number is missing in the progression?')

    for _ in range(1, 4):
        first = random.randint(1, 20)
        step = random.randint(1, 15)
        iterations = random.randint(5, 10)
        progression = get_progression(first, step, iterations)
        stack.append([progression[0], progression[1]])
    return stack
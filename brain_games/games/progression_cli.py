import random


def get_progression(first_number: int, step: int, iterations: int) -> list:
    levels_information = []
    position = random.randint(1, iterations)
    number = 0
    progression = ''
    for i in range(1, iterations + 1):
        if i == position:
            progression += '.. '
            number += first_number
            first_number += step
            continue
        progression += str(first_number) + ' '
        first_number += step
    levels_information += [progression, number]
    return levels_information


def brain_progression_game() -> list:
    games_information = []
    games_information.append('What number is missing in the progression?')
    for _ in range(1, 4):
        first_number = random.randint(1, 20)
        step = random.randint(1, 15)
        iterations = random.randint(5, 10)
        question, answer = get_progression(first_number, step, iterations)
        games_information.append([question, answer])
    return games_information
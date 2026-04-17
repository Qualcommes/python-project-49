import random


def get_gcd(first_number: int, second_number: int) -> int:
    while second_number != 0:
        value = first_number
        first_number = second_number
        second_number = value % second_number
    return first_number


def brain_gcd_game() -> list:
    games_information = []
    games_information.append('Find the ' 
    'greatest common divisor of given numbers.')
    for _ in range(1, 4):
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        answer = get_gcd(first_number, second_number)
        question = str(first_number) + ' ' + str(second_number)
        games_information.append([question, answer])
    return games_information
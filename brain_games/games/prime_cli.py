import random


def is_prime(number: int) -> str:
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 
                 19, 23, 29, 31, 37, 41, 
                 43, 47, 53, 59, 61, 67, 
                 71, 73, 79, 83, 89, 97, 
                 101, 103, 107, 109]
    if number in prime_numbers:
        return 'yes'
    return 'no'


def brain_prime_game() -> list:
    games_information = []
    games_information.append('Answer "yes" if given number '
    'is prime. Otherwise answer "no".')
    for _ in range(1, 4):
        question = random.randint(1, 110)
        answer = is_prime(question)
        games_information.append([question, answer])
    return games_information
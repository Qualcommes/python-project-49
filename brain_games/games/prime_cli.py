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
    stack = []
    stack.append('Answer "yes" if given number '
    'is prime. Otherwise answer "no".')
    for _ in range(1, 4):
        number = random.randint(1, 110)
        result = is_prime(number)
        stack.append([number, result])
    return stack
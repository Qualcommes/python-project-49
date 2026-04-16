import random


def get_gcd(a: int, b: int) -> int:
    while b != 0:
        value = a
        a = b
        b = value % b
    return a


def brain_gcd_game() -> list:
    stack = []
    stack.append('Find the greatest common divisor of given numbers.')
    for i in range(1, 4):
        number = random.randint(1, 100)
        number2 = random.randint(1, 100)
        gcd = get_gcd(number, number2)
        expression = str(number) + ' ' + str(number2)
        stack.append([expression, gcd])
    return stack
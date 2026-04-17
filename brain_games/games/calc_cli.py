import random


def get_expression() -> list:
    levels_information = []
    expression = ''
    result = 0
    number = random.randint(1, 30)
    number2 = random.randint(1, 30)
    operation = random.randint(1, 3)
    match operation:
        case 1: 
            expression = str(number) + ' + ' + str(number2)
            result += number + number2
        case 2: 
            expression = str(number) + ' - ' + str(number2)
            result += number - number2
        case 3: 
            expression = str(number // 2) + ' * ' + str(number2 // 2)
            result += (number // 2) * (number2 // 2)
    levels_information += [expression, result]
    return levels_information


def brain_calc_game() -> list:
    games_information = []
    games_information.append('What is the result of the expression?')
    for _ in range(1, 4):
        question, answer = get_expression()
        games_information.append([question, answer])
    return games_information


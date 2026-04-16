import random


def get_expression() -> list:
    stack = []
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
    stack += [expression, result]
    return stack


def brain_calc_game() -> list:
    stack = []
    stack.append('What is the result of the expression?')
    for i in range(1, 4):
        expression = get_expression()
        stack.append([expression[0], expression[1]])
    return stack


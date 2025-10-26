import random

import prompt


def is_even(number: int) -> str:
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def brain_even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    i = 0
    while i <= 3:
        if i == 3:
            print("Congratulations, " + name + "!")
            break
        number = random.randint(1, 100)
        print("Question: " + str(number))
        answer = prompt.string('Your answer: ')
        correct_answer = is_even(number)
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print("'" + answer + "' is wrong answer ;(."
                    "Correct answer was '" + correct_answer + "'.")
            print("Let's try again, " + name + "!")
            break


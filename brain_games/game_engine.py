import prompt


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print("Hello, " + name + "!")
    return name


def game(game_information: list):
    name = welcome_user()
    print(game_information[0])
    for i in range(1, 4):
        answer = prompt.string('Question: ' + 
                               str(game_information[i][0]) + '\nYour answer: ')
        if answer == str(game_information[i][1]):
            print('Correct!')
        else:
            print("'" + answer + "' is wrong answer ;(."
                    "Correct answer was '" + 
                    str(game_information[i][1]) + "'.")
            print("Let's try again, " + name + "!")
            return
    print('Congratulations, ' + name + '!')
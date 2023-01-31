from brain_games.cli import welcome_user
from random import randint


def is_even(question_even_number):
    if question_even_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def game_even_go():
    counter = 0
    name = welcome_user()
    while counter < 3:
        question_even_number = randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question: ', question_even_number)
        answer = input()
        is_even(question_even_number)
        correct_answer = is_even(question_even_number)
        if answer != correct_answer:
            print(f'''"{answer}" is wrong answer. Correct answer was "{correct_answer}". Let's try again, {name}!''')
            return
        else:
            print('Correct!')
            counter = counter + 1
    else:
        print(f'''Congratulations, {name}!''')


def main():
    print('Welcome to the Brain Games!')
#   welcome_user()
    game_even_go()


if __name__ == '__main__':
    main()

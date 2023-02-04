from brain_games.cli import welcome_user
from random import randint


def is_prime(question_prime_number):
    counter_prime = 0
    for i in range(2, question_prime_number):
        if question_prime_number%i == 0:
            counter_prime = counter_prime+1
    if counter_prime <= 0:
            correct_answer = 'yes'
    else:
            correct_answer = 'no'
    return correct_answer


def game_prime_go():
    counter = 0
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while counter < 3:
        question_prime_number = randint(1, 100)
        print('Question: ', question_prime_number)
        answer = input()
        is_prime(question_prime_number)
        correct_answer = is_prime(question_prime_number)
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
    game_prime_go()


if __name__ == '__main__':
    main()

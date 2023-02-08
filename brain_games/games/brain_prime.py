from brain_games.cli import welcome_user
from random import randint


def gen_quest_answer():
    question = randint(1, 100)
    counter_prime = 0
    for i in range(2, question):
        if question % i == 0:
            counter_prime = counter_prime + 1
    if counter_prime <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def game_condition():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def main():
    print('Welcome to the Brain Games!')
    game_go()


if __name__ == '__main__':
    main()

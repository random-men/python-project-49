from brain_games.cli import welcome_user
from random import randint
import math

def gen_quest_answer():
    question_gcd_number1 = randint(1, 100)
    question_gcd_number2 = randint(1, 100)
    question = f'{question_gcd_number1} {question_gcd_number2}'
    correct_answer = math.gcd(question_gcd_number1, question_gcd_number2)
    return question, correct_answer

def game_condition():
    print('Find the greatest common divisor of given numbers.')


def main():
    print('Welcome to the Brain Games!')
    game_go()


if __name__ == '__main__':
    main()



from random import randint
import math

def game_condition():
    print('Find the greatest common divisor of given numbers.')

def gen_quest_answer():
    question_gcd_number1 = randint(1, 100)
    question_gcd_number2 = randint(1, 100)
    question = f'{question_gcd_number1} {question_gcd_number2}'
    correct_answer = math.gcd(question_gcd_number1, question_gcd_number2)
    return question, correct_answer
from brain_games.cli import welcome_user
from random import randint

def game_condition():
    print('Answer "yes" if the number is even, otherwise answer "no".')

def gen_quest_answer():
    question_even_number = randint(1, 100)
    question = question_even_number
    if question_even_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer



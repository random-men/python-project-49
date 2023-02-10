from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game():
    question_even_number = randint(1, 100)
    question = question_even_number
    if question_even_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

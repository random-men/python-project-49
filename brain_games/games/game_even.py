from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question_even_number):
    if question_even_number % 2 == 0:
        return True
    else:
        return False


def generate_game():
    question_even_number = randint(1, 100)
    question = question_even_number
    correct_answer = is_even(question_even_number)
    if is_even(question_even_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


from random import randint, choice

GAME_RULE = 'What is the result of the expression?'
QUESTION_OPERATOR = ('+', '-', '*')


def calculate_expression(question_calc_number1,
                         question_calc_number2,
                         final_calc_operation):
    if final_calc_operation == '+':
        correct_answer = question_calc_number1 + question_calc_number2
    elif final_calc_operation == '-':
        correct_answer = question_calc_number1 - question_calc_number2
    else:
        correct_answer = question_calc_number1 * question_calc_number2
    return correct_answer


def generate_game():
    question_calc_number1 = randint(1, 10)
    question_calc_number2 = randint(1, 10)
    final_calc_operation = choice(QUESTION_OPERATOR)
    question = f'{question_calc_number1} ' \
               f'{final_calc_operation} ' \
               f'{question_calc_number2}'
    correct_answer = calculate_expression(question_calc_number1,
                                          question_calc_number2,
                                          final_calc_operation)
    return question, correct_answer

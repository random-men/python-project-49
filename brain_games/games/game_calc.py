
from random import randint

GAME_RULE = 'What is the result of the expression?'

def gen_quest_answer():
    question_calc_number1 = randint(1, 10)
    question_calc_number2 = randint(1, 10)
    question_calc_operation = ('+', '-', '*')
    choice_operation_index = randint(0, 2)
    final_calc_operation = question_calc_operation[choice_operation_index]
    question = f'{question_calc_number1} {final_calc_operation} {question_calc_number2}'
    if final_calc_operation == '+':
        correct_answer = question_calc_number1 + question_calc_number2
    elif final_calc_operation == '-':
        correct_answer = question_calc_number1 - question_calc_number2
    else:
        correct_answer = question_calc_number1 * question_calc_number2
    return question, correct_answer
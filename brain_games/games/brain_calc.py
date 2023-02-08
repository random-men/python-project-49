from brain_games.cli import welcome_user
from random import randint


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


def game_condition():
    print('What is the result of the expression?')




def main():
    game_go()


if __name__ == '__main__':
    main()

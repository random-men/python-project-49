from brain_games.cli import welcome_user
from random import randint


def calculate_answer(question_calc_number1, question_calc_number2, final_calc_operation):
    if final_calc_operation == '+':
        correct_answer = question_calc_number1 + question_calc_number2
    elif final_calc_operation == '-':
        correct_answer = question_calc_number1 - question_calc_number2
    else:
        correct_answer = question_calc_number1 * question_calc_number2
    return correct_answer


def game_calc_go():
    counter = 0
    name = welcome_user()
    print('What is the result of the expression?')
    while counter < 3:
        question_calc_number1 = randint(1, 10)
        question_calc_number2 = randint(1, 10)
        question_calc_operation = ('+', '-', '*')
        choice_operation_index = randint(0, 2)
        final_calc_operation = question_calc_operation[choice_operation_index]
        print(f'''Question: {question_calc_number1} {final_calc_operation} {question_calc_number2}''')
        answer = input()
        calculate_answer(question_calc_number1, question_calc_number2, final_calc_operation)
        correct_answer = calculate_answer(question_calc_number1, question_calc_number2, final_calc_operation)
        if int(answer) != correct_answer:
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
    game_calc_go()


if __name__ == '__main__':
    main()

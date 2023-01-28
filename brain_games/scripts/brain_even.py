from brain_games.scripts.brain_games import main
from random import randint

def is_even(question_even_number):
    global correct_answer
    if question_even_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer

counter = 0
while counter < 3:
    question_even_number = randint(1, 100)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: ', question_even_number)
    answer = input()
    is_even(question_even_number) 
    if answer != correct_answer:
        print(f'"{answer}" is wrong answer. Correct answer was "{correct_answer}"')
        break
    else:
        print('Correct!')
        counter = counter + 1
else:
    print('Congratulations! All 3 answers were correct!')

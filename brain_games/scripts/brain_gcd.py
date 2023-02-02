from brain_games.cli import welcome_user
from random import randint
import math

def game_gcd_go():
    counter = 0
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    while counter < 3:
        question_gcd_number1 = randint(1, 100)
        question_gcd_number2 = randint(1, 100)
        print(f'''Question: {question_gcd_number1} {question_gcd_number2}''')
        answer = input()
        correct_answer = math.gcd(question_gcd_number1, question_gcd_number2) 
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
    game_gcd_go()


if __name__ == '__main__':
    main()

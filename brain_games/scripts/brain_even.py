from brain_games.scripts.brain_games import main
from brain_games.cli import welcome_user
from random import randint

question_even_number = randint(1, 100)
print('Answer "yes" if the number is even, otherwise answer "no".')
print('Question: ', question_even_number)
answer = input()



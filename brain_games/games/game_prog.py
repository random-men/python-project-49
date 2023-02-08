from brain_games.cli import welcome_user
from random import randint

def game_condition():
    print('What number is missing in the progression?')

def gen_quest_answer():
    quest_prog_start = randint(1, 80)
    quest_prog_iter = randint(1, 9)
    quest_index = randint(0, 4)
    question = [quest_prog_start]
    quest_prog_length = len(question)
    while len(question) < 5:
        for i in range(quest_prog_length):
            n = quest_prog_start + quest_prog_iter
            question.append(n)
            quest_prog_start = n
    correct_answer = question[quest_index]
    question[quest_index] = 'XX'
    return question, correct_answer



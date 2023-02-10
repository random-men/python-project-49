from random import randint

GAME_RULE = 'What number is missing in the progression?'


def generate_progression():
    quest_prog_start = randint(1, 80)
    quest_prog_iter = randint(1, 9)
    progression = [quest_prog_start]
    quest_prog_length = len(progression)
    while len(progression) < 5:
        for i in range(quest_prog_length):
            n = quest_prog_start + quest_prog_iter
            progression.append(n)
            quest_prog_start = n
    return progression


def generate_game():
    quest_index = randint(0, 4)
    progression = generate_progression()
    correct_answer = progression[quest_index]
    progression[quest_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer

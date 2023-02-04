from brain_games.cli import welcome_user
from random import randint


def gen_prog(question_prog_start, question_prog_iter, question_index):
    gen_quest_prog = [question_prog_start]
    quest_prog_length = len(gen_quest_prog)
    while len(gen_quest_prog) < 5:
        for i in range(quest_prog_length):
            n = question_prog_start + question_prog_iter
            gen_quest_prog.append(n) 
            question_prog_start = n  
    correct_answer = gen_quest_prog[question_index]
    gen_quest_prog[question_index] =  'XX'
    return gen_quest_prog, correct_answer


def game_prog_go():
    counter = 0
    name = welcome_user()
    print('What number is missing in the progression?')
    while counter < 3:
        question_prog_start = randint(1, 80)
        question_prog_iter = randint(1, 9)
        question_index = randint(0, 4)
        gen_quest_prog, correct_answer = gen_prog(question_prog_start, question_prog_iter, question_index) 
        print(f'''Question: {gen_quest_prog}''') 
        answer = input()       
        if int(answer) != correct_answer:
            print(f'''"{answer}" is wrong answer. Correct answer was "{correct_answer}". Let's try again, {name}!''')
            return
        else:
            print('Correct!')
            counter = counter + 1


def main():
    print('Welcome to the Brain Games!')
#   welcome_user()
    game_prog_go()


if __name__ == '__main__':
    main()

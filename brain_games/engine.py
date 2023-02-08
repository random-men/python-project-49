import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name



game_condition()

def game_go():
    name = welcome_user()
    counter_rounds = 0
    while counter_rounds < 3:
        question, correct_answer = gen_quest_answer()
        print(f'''Question: {question}''')
        answer = input()
        if int(answer) != correct_answer:
            print(f'''"{answer}" is wrong answer. Correct answer was "{correct_answer}". Let's try again, {name}!''')
            return
        else:
            print('Correct!')
            counter_rounds = counter_rounds + 1
    else:
        print(f'''Congratulations, {name}!''')
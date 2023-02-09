import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_go(game):
    name = welcome_user()
    print(game.GAME_RULE)
    counter_rounds = 0
    while counter_rounds < 3:
        question, correct_answer = game.gen_quest_answer()
        print(f'''Question: {question}''')
        answer = input()
        if answer != str(correct_answer):
            print(f'''"{answer}" is wrong answer. '''
                  f'''Correct answer was "{correct_answer}".''')
            print(f'''Let's try again, {name}!''')
            return
        else:
            print('Correct!')
            counter_rounds = counter_rounds + 1
    else:
        print(f'''Congratulations, {name}!''')

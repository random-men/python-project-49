from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_game():
    question = randint(2, 100)
    counter_prime = 0
    for i in range(2, question):
        if question % i == 0:
            counter_prime = counter_prime + 1
    if counter_prime <= 1:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

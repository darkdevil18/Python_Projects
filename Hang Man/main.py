import random

import art

from hangman_art import stages
from hangman_words import word_list

choosen_word = random.choice(word_list)

choosen_word_length = len(choosen_word)
guess_word_list = []
for _ in range(choosen_word_length):
    guess_word_list += '_'

game_over = False
available_lives = 6

while not game_over:
    art.tprint('hangman')
    # print(logo)
    guess = input('Guess a letter : ').lower()

    if guess in guess_word_list:
        print("You have already guessed {}.".format(guess))
        print(stages[available_lives])
        continue

    wrong_guess = False

    if guess in choosen_word:
        for i in range(choosen_word_length):
            letter = choosen_word[i]
            if letter == guess:
                guess_word_list[i] = guess
    else:
        wrong_guess = True

    if not wrong_guess:
        print(f"{guess} is a correct guess.")
        # print(stages[available_lives])

    if wrong_guess:
        available_lives -= 1
        print(f"Your guess {guess} is wrong. You loose one life.")

    print(''.join(guess_word_list))
    print(stages[available_lives])

    if available_lives == 0:
        game_over = True
        print("Better Luck Next Time.")

    if guess_word_list.count('_') == 0:
        print("Congratulations!!! You won.")
        game_over = True

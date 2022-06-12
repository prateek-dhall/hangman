# Creating a hangman aka word guessing game
import random
from words import words
import string

def valid_word(w): 
    selected_word = random.choice(w)
    while '-' in selected_word or ' ' in selected_word:
        selected_word = random.choice(w)
    return selected_word.upper()

def hangman():
    word_generated = valid_word(words)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    word_letters = set(word_generated)
    lives = 6
    
    while len(word_letters)>0 and lives>0:
        print('Letter guessed till now:', ', '.join(used_letters),' | ', end=' ')
        print(f'Lives left = {lives}')

        word_print = [letter if letter in used_letters else '-' for letter in word_generated]
        print("Word to be guessed: ",' '.join(word_print))

        user_input = input('Enter a letter between A-Z: ').upper()

        if user_input in alphabets:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            elif user_input not in word_letters:
                lives = lives-1
        elif user_input in used_letters:
            print("Entered letter is already guessed, Try Again !!!!")
        else:
            print('You have entered a wrong value, Try Again.....!!!!!')
    if lives == 0:
        print("No lives left, YOU LOST !!!!")
    else:
        print("Congratulations, YOU WON !!!")

hangman()
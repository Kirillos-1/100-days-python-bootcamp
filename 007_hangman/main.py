import random
import art
from words import word_list


def getting_word(word_list: list) -> str:
    return random.choice(word_list)


def validating_guess(prompt: str) -> str:
    while True:
        guess = input(prompt).strip().lower()
        
        if guess == "":
            print('Please enter a letter. Input cannot be empty.')
            continue
            
        if len(guess) != 1:
            print('Please enter only one letter.')
            continue
        
        if not guess.isalpha():
            print('Please enter a valid letter (a-z).')
            continue
        
        return guess


def main() -> None:
    print(art.logo)
    print('Welcome to the Hangman Game!\n')

    word_to_guess = getting_word(word_list)
    placeholder = ["_"] * len(word_to_guess)
    guessed_letters = []
    lives = 6
    
    while lives > 0 and "_" in placeholder:
        print('\nWord:', ''.join(placeholder))   
        print(f'Lives remaining: {lives}')
        print('Guessed letters:', ', '.join(sorted(guessed_letters)) if guessed_letters else 'None')

        guess = validating_guess('Guess a letter: ')

        if guess in guessed_letters:
            print(f'You already guessed \'{guess}\'. Try another.')
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print(f'Good guess! \'{guess}\' is in the word.')

            for index in range(len(word_to_guess)):
                if word_to_guess[index] == guess:
                    placeholder[index] = guess
        else:
            lives -= 1
            print(f'Wrong guess! \'{guess}\' is not in the word.')
            print(art.stages[lives])

        
    if "_" not in placeholder:
        print('\nCongratulations! You guessed the word:')
        print(''.join(placeholder))
    else:
        print('\nGame over!')
        print(f'The word was: {word_to_guess}')


main()
import os
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_choice(prompt: str, valid_choices: set[str]) -> str:
    """Keep asking until the user enters one of the valid choices."""
    while True:
        choice = input(prompt).strip().lower()

        if choice in valid_choices:
            return choice

        print(f"Invalid choice. Please enter one of: {', '.join(sorted(valid_choices))}")


def set_difficulty() -> int:
    """Return the number of attempts based on the selected difficulty."""
    choice = get_choice(
        "Choose difficulty. Type 'easy' or 'hard': ",
        {"easy", "hard"}
    )

    if choice == "easy":
        return EASY_LEVEL_TURNS

    return HARD_LEVEL_TURNS


def get_guess(prompt: str, min_number: int, max_number: int) -> int:
    """Keep asking until the user enters a valid number inside the allowed range."""
    while True:
        guess_text = input(prompt).strip()

        try:
            guess = int(guess_text)
        except ValueError:
            print(f"Please enter a valid whole number between {min_number} and {max_number}.")
            continue

        if min_number <= guess <= max_number:
            return guess

        print(f"Your guess must be between {min_number} and {max_number}.")


def check_guess(user_guess: int, answer: int) -> bool:
    """
    Compare the user's guess with the answer.

    Return True if the guess is correct.
    Return False if the guess is wrong.
    """
    if user_guess > answer:
        print("Too high.")
        return False

    if user_guess < answer:
        print("Too low.")
        return False

    print(f"You got it! The answer was {answer}.")
    return True


def play_game() -> None:
    """Run one full round of the Number Guessing Game."""
    clear_screen()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.\n")

    answer = randint(MIN_NUMBER, MAX_NUMBER)
    turns = set_difficulty()

    while turns > 0:
        print(f"\nYou have {turns} attempts remaining to guess the number.")

        user_guess = get_guess(
            f"Make a guess ({MIN_NUMBER}-{MAX_NUMBER}): ",
            MIN_NUMBER,
            MAX_NUMBER
        )

        is_correct = check_guess(user_guess, answer)

        if is_correct:
            return

        turns -= 1

        if turns > 0:
            print("Guess again.")
        else:
            print("\nYou have run out of attempts.")
            print(f"You lose. The answer was {answer}.")


def main() -> None:
    """Control replaying the game."""
    while True:
        play_game()

        play_again = get_choice(
            "\nDo you want to play again? Type 'y' or 'n': ",
            {"y", "n"}
        )

        if play_again == "n":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
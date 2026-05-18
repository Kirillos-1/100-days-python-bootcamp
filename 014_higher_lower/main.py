from art import logo, vs
from data import data
import random
import os


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_random_account(exclude: dict | None = None) -> dict:
    """
    Return a random account from teh data list.
    
    if exclude is provided, make sure the same account is not selected again.
    """
    account = random.choice(data)

    while exclude is not None and account == exclude:
        account = random.choice(data)

    return account


def format_account(account: dict) -> str:
    """Return a readable account description without showing follower count."""
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"


def get_user_choice() -> str:
    """Keep asking until the user chooses A or B."""
    while True:
        choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()

        if choice in {"a", "b"}:
            return choice
        
        print("Invalid choice. Please type 'A' or 'B'.")


def has_more_followers(account_a: dict, account_b: dict) -> str:
    """Return 'a' if account A has more followers, otherwise return 'b'."""
    if account_a["follower_count"] > account_b["follower_count"]:
        return "a"
    
    return "b"

def check_answer(user_choice: str, correct_choice: str) -> bool:
    """Return True if the user's choice is correct."""
    return user_choice == correct_choice


def play_game() -> None:
    """Run one full round of the Higher Lower game."""
    score = 0
    game_over = False
    
    account_a = get_random_account()
    account_b = get_random_account(exclude=account_a)

    while not game_over:
        clear_screen()
        print(logo)

        if score > 0:
            print(f"You're right! Current score: {score}\n")

        print(f"Compare A: {format_account(account_a)}.")
        print(vs)
        print(f"Against B: {format_account(account_b)}.\n")

        user_choice = get_user_choice()
        correct_choice = has_more_followers(account_a, account_b)

        if check_answer(user_choice, correct_choice):
            score += 1
            
            if correct_choice == "b":
                account_a = account_b
                
            account_b = get_random_account(exclude=account_a)
        
        else:
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
            

def main() -> None:
    """Control replaying the game."""
    while True:
        play_game()

        while True:
            again = input("\nDo you want to play again? Type 'y' or 'n': ").strip().lower()

            if again in {"y", "n"}:
                break

            print("Invalid choice. Please type 'y' or 'n'.")

        if again == "n":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
    
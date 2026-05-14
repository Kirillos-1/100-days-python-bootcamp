import os
import random
from art import logo


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_choice(prompt: str, valid_choices: set[str]) -> str:
    """Keep asking until the user enters a valid choice."""
    while True:
        choice = input(prompt).strip().lower()

        if choice in valid_choices:
            return choice

        print(f"Invalid choice. Please enter one of: {', '.join(sorted(valid_choices))}")


def deal_card() -> int:
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards: list[int]) -> int:
    """Calculate the score of a hand and handle Ace logic."""
    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def decide_winner(user_score: int, computer_score: int) -> str:
    """Compare user and dealer scores and return the result."""
    if user_score == computer_score:
        return "Draw."
    if computer_score == 0:
        return "You lose. Dealer has Blackjack."
    if user_score == 0:
        return "You win with Blackjack."
    if user_score > 21:
        return "You lose. You went over 21."
    if computer_score > 21:
        return "You win. Dealer went over 21."
    if user_score > computer_score:
        return "You win."

    return "You lose."


def play_game() -> None:
    """Run one round of Blackjack."""
    clear_screen()
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while not game_over:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = get_choice(
                "Type 'y' to get another card, type 'n' to pass: ",
                {"y", "n"}
            )

            if should_continue == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)

                clear_screen()
                print(logo)
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
    print(decide_winner(user_score, computer_score))


def main() -> None:
    """Control replaying the Blackjack game."""
    while True:
        play = get_choice("Do you want to play Blackjack? Type 'y' or 'n': ", {"y", "n"})

        if play == "y":
            play_game()
        else:
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
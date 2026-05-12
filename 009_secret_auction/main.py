from art import logo
import os


bidders_info = {}


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def validate_bidder_name(prompt: str) -> str:
    while True:
        name = input(prompt).strip().title()

        if len(name) < 2:
            print("Please, enter a valid name. 2 characters or more.")
            continue

        if not name.isalpha():
            print("Please, enter a valid name containing alpha letters only.")
            continue

        return name


def validate_bidder_amount(prompt: str) -> float:
    while True:
        bidder_amount = input(prompt).strip()

        try:
            bidder_amount = float(bidder_amount)
        except ValueError:
            print("Please, enter a valid number.")
            continue

        if bidder_amount <= 0:
            print("Please, enter an amount greater than 0.")
            continue

        return bidder_amount


def get_winner(bidders_info: dict) -> tuple[str, float]:
    winner_name = ""
    highest_bid = 0

    for name, amount in bidders_info.items():
        if amount > highest_bid:
            highest_bid = amount
            winner_name = name

    return winner_name, highest_bid


def main() -> None:
    print(logo)
    print("Welcome to the secret auction program!\n")

    while True:
        bidder_name = validate_bidder_name("What's the bidder name: ")
        bidder_amount = validate_bidder_amount("What's the bid amount: $")

        bidders_info[bidder_name] = bidder_amount

        while True:
            another_bidder = input(
                "Are there any other bidders? Type 'yes' or 'no': "
            ).strip().lower()

            if another_bidder in ["yes", "no"]:
                break

            print("Please, type only 'yes' or 'no'.")

        if another_bidder == "yes":
            clear_screen()
            print(logo)
        else:
            break

    winner_name, highest_bid = get_winner(bidders_info)

    clear_screen()
    print(logo)
    print("Auction finished!\n")
    print(f"The winner is {winner_name} with a bid of ${highest_bid:.2f}")


main()
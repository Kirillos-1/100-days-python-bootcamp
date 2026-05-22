from data import MENU, resources
from art import logo
import os


VALID_COMMANDS = ["espresso", "latte", "cappuccino", "report", "off"]

COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_user_choice() -> str:
    """Ask the user what they want and return a valid command."""
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

        if choice in VALID_COMMANDS:
            return choice
        
        print("Invalid input. Please choose: espresso, latte, cappuccino.")
    

def print_report() -> None:
    """Print the current machine resources."""
    print("=================== REPORT ===================")
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}gm")
    print(f"Coins: {resources["money"]:.2f}")
    print("==============================================")


def check_resources(user_choice: str) -> bool:
    """Return True if there are enough resources to make the selected drink."""
    required_resources = MENU[user_choice]["ingredients"]

    for ingredient, required_amount in required_resources.items():
        if resources[ingredient] < required_amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        
    return True


def get_coin_count(coin_name: str) -> int:
    """Keep asking until the user enters a valid non-negative number of coins."""
    while True:
        coin_count = input(f"How many {coin_name}: ").strip()

        try:
            coin_count = int(coin_count)
        except ValueError:
            print("Please enter a valid whole number.")
            continue
        
        if coin_count >= 0:
            return coin_count
        
        print("Coin count cannot be negative.")


def process_coins() -> float:
    """Ask the user for coins and return the total inserted money."""
    print("Please insert coins:\n")

    total = 0
    
    for coin_name, coin_value in COIN_VALUES.items():
        coin_count = get_coin_count(coin_name)
        total += coin_count * coin_value
        
    return round(total, 2)


def check_transactions(user_choice: str, money_inserted: float) -> bool:
    """Return True if the user inserted enough money for the selected drink."""
    drink_cost = MENU[user_choice]["cost"]
    
    if money_inserted < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    change = round(money_inserted - drink_cost, 2)
    
    if change > 0:
        print(f"Here is ${change} dollars in change.")

    resources["money"] += drink_cost
    resources["money"] = round(resources["money"], 2)

    return True


def make_coffee(user_choice: str) -> None:
    """Deduct ingredients from resources and serve the selected drink."""
    required_ingredients = MENU[user_choice]["ingredients"]
    
    for ingredient, required_amount in required_ingredients.items():
        resources[ingredient] -= required_amount
        
    print(f"Here is your {user_choice}. Enjoy!")


def serve_drink(user_choice: str) -> None:
    """Handle the full drink order process"""
    if not check_resources(user_choice):
        return
    
    money_inserted = process_coins()

    if check_transactions(user_choice, money_inserted):
        make_coffee(user_choice)

def main() -> None:
    """Run the coffee machine program."""
    clear_screen()
    print(logo)
    
    machine_on = True
    
    while machine_on:
        choice = get_user_choice()
        
        if choice == "off":
            machine_on = False
            print("Coffee machine turned off.")
        elif choice == "report":
            print_report()
        else:
            serve_drink(choice)
            

if __name__ == "__main__":
    main()
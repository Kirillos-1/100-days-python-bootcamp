import os
from art import logo

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_user_choice(options: str) -> str:
    """Return a valid user command or menu choice."""
    clean_options = options.rstrip("/")
    valid_choices = set(clean_options.split("/"))
    valid_choices.update({"off", "report"})

    while True:
        choice = input(f"What would you like? ({clean_options}): ").strip().lower()

        if choice in valid_choices:
            return choice

        print("Invalid choice. Please choose a drink, 'report', or 'off'.")


def print_full_report(coffee_maker: CoffeeMaker, money_machine: MoneyMachine) -> None:
    """Print resources and money report."""
    print("\n========== MACHINE REPORT ==========")
    coffee_maker.report()
    money_machine.report()
    print("====================================\n")


def serve_order(drink_name: str, menu: Menu, coffee_maker: CoffeeMaker, money_machine: MoneyMachine) -> None:
    """Find the drink, check resources, process payment, and make coffee."""
    drink = menu.find_drink(drink_name)

    if drink is None:
        return

    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)


def main() -> None:
    """Run the OOP Coffee Machine program."""
    clear_screen()
    print(logo, "\n")

    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    machine_on = True

    while machine_on:
        options = menu.get_items()
        choice = get_user_choice(options)

        if choice == "off":
            machine_on = False
            print("Coffee machine turned off.")

        elif choice == "report":
            print_full_report(coffee_maker, money_machine)

        else:
            serve_order(choice, menu, coffee_maker, money_machine)


if __name__ == "__main__":
    main()
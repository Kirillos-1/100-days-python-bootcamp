from art import logo


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


OPERATORS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid number.")


def get_operator() -> str:
    while True:
        operator = input(
            "Pick an operator:\n"
            "+\n"
            "-\n"
            "*\n"
            "/\n"
            "Your choice: "
        ).strip()

        if operator in OPERATORS:
            return operator

        print("Invalid operator. Please choose one of: +, -, *, /")


def get_continue_choice(result: float) -> str:
    while True:
        choice = input(
            f"\nType 'y' to continue calculating with {result:.2f},\n"
            "type 'n' to start a new calculation,\n"
            "or type 'q' to quit: "
        ).strip().lower()

        if choice in ("y", "n", "q"):
            return choice

        print("Invalid choice. Please type 'y', 'n', or 'q'.")


def main() -> None:
    print(logo)

    while True:
        num1 = get_number("What's the first number? ")

        while True:
            operator = get_operator()
            num2 = get_number("What's the second number? ")

            operation_function = OPERATORS[operator]

            try:
                result = operation_function(num1, num2)
            except ZeroDivisionError as error:
                print(error)
                continue

            print(f"\n{num1} {operator} {num2} = {result:.2f}")

            choice = get_continue_choice(result)

            if choice == "y":
                num1 = result

            elif choice == "n":
                print("\nStarting a new calculation...\n")
                break

            elif choice == "q":
                print("\nCalculator turned off. Goodbye!")
                return


main()
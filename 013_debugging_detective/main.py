import os
from art import logo

VALID_BUG_TYPES = {"syntax", "logic", "type", "index", "scope"}

BUG_CASES = [
    {
        "title": "Case 01 - The Silent Total",
        "code": """numbers = [10, 20, 30]
total = 0

for number in numbers:
    total + number

print(total)""",
        "bug_type": "logic",
        "hint": "The code runs, but the total never changes.",
        "explanation": "The expression `total + number` calculates a value but does not store it. It should be `total += number`.",
    },
    {
        "title": "Case 02 - The Broken Greeting",
        "code": """name = "Kirillos"
print("Hello, " + name""",
        "bug_type": "syntax",
        "hint": "The program cannot even start running.",
        "explanation": "The `print()` call is missing a closing parenthesis.",
    },
    {
        "title": "Case 03 - The Age Problem",
        "code": """age = input("Enter your age: ")

if age >= 18:
    print("Access granted.")
else:
    print("Access denied.")""",
        "bug_type": "type",
        "hint": "Remember what type `input()` returns.",
        "explanation": "`input()` returns a string. Convert it first using `int()` before comparing it with 18.",
    },
    {
        "title": "Case 04 - The Last Item Crash",
        "code": """items = ["keyboard", "mouse", "monitor"]

for index in range(1, 4):
    print(items[index])""",
        "bug_type": "index",
        "hint": "Python list indexes start from 0.",
        "explanation": "The list has indexes 0, 1, and 2. The loop reaches index 3, which causes an IndexError.",
    },
    {
        "title": "Case 05 - The Missing Variable",
        "code": """def calculate_score():
    score = 10

calculate_score()
print(score)""",
        "bug_type": "scope",
        "hint": "Where was `score` created?",
        "explanation": "`score` is local to the function. It cannot be accessed outside unless it is returned or defined globally.",
    },
]


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_choice(prompt: str, valid_choices: set[str]) -> str:
    """Keep asking until the user enters a valid choice."""
    while True:
        choice = input(prompt).strip().lower()

        if choice in valid_choices:
            return choice

        print(f"Invalid choice. Choose one of: {', '.join(sorted(valid_choices))}")


def show_bug_types() -> None:
    """Display the available bug categories."""
    print("Bug types:")
    print("- syntax : code structure is invalid")
    print("- logic  : code runs, but the result is wrong")
    print("- type   : wrong data type is used")
    print("- index  : invalid list/string position is accessed")
    print("- scope  : variable is used outside where it exists")


def run_case(case: dict[str, str], case_number: int, total_cases: int) -> bool:
    """Run one debugging case and return True if the user is correct."""
    print(f"\n[{case_number}/{total_cases}] {case['title']}")
    print("-" * 60)
    print(case["code"])
    print("-" * 60)

    want_hint = get_choice("Do you want a hint? Type 'y' or 'n': ", {"y", "n"})

    if want_hint == "y":
        print(f"Hint: {case['hint']}")

    show_bug_types()
    answer = get_choice("\nWhat type of bug is this? ", VALID_BUG_TYPES)

    if answer == case["bug_type"]:
        print("\nCorrect.")
        print(f"Explanation: {case['explanation']}")
        return True

    print("\nNot quite.")
    print(f"Correct answer: {case['bug_type']}")
    print(f"Explanation: {case['explanation']}")
    return False


def play_game() -> None:
    """Run the full debugging detective game."""
    clear_screen()
    print(logo)
    print("Welcome to Debugging Detective.")
    print("Your mission: inspect each code case and identify the bug type.")

    score = 0
    total_cases = len(BUG_CASES)

    for index, case in enumerate(BUG_CASES, start=1):
        solved = run_case(case, index, total_cases)

        if solved:
            score += 1

        if index < total_cases:
            input("\nPress Enter to continue to the next case...")
            clear_screen()
            print(logo)

    print("\nMission complete.")
    print(f"Final score: {score}/{total_cases}")

    if score == total_cases:
        print("Perfect run. Clean debugging work.")
    elif score >= total_cases // 2:
        print("Good work. You are building the debugging mindset.")
    else:
        print("Keep practicing. Debugging gets stronger with repetition.")


def main() -> None:
    """Control replaying the project."""
    while True:
        play_game()
        again = get_choice("\nDo you want to debug another round? Type 'y' or 'n': ", {"y", "n"})

        if again == "n":
            print("Goodbye, detective.")
            break


if __name__ == "__main__":
    main()

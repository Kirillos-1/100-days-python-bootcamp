# Day 12 - Number Guessing Game

This is my solution for **Day 12** of the **100 Days of Code: Python Bootcamp by Angela Yu**.

Day 12 focuses on **scope** in Python and applies it through a command-line **Number Guessing Game**. The player tries to guess a hidden number between 1 and 100, with the number of attempts depending on the selected difficulty.

I tried to make the game cleaner than the basic version by adding input validation, constants, helper functions, and a clear game loop.

---

## Project Idea

The program randomly chooses a number between 1 and 100.

The player chooses a difficulty level:

- **Easy:** 10 attempts
- **Hard:** 5 attempts

After each guess, the program tells the player whether the guess is too high, too low, or correct. The game ends when the player guesses the number correctly or runs out of attempts.

---

## What I Practiced

Through this project, I practiced:

- Python scope
- Constants
- Random number generation
- Functions with return values
- Input validation
- `try` / `except` error handling
- Game loops
- Difficulty-based logic
- Cleaner function separation
- Writing a more user-friendly command-line program

---

## Functions Used

The project is organized around these main functions:

| Function           | Purpose                                                              |
| ------------------ | -------------------------------------------------------------------- |
| `clear_screen()`   | Clears the terminal screen for a cleaner experience                  |
| `get_choice()`     | Validates text choices like difficulty and replay input              |
| `set_difficulty()` | Returns the number of attempts based on easy or hard mode            |
| `get_guess()`      | Keeps asking until the user enters a valid number in range           |
| `check_guess()`    | Compares the guess with the answer and returns whether it is correct |
| `play_game()`      | Runs one complete round of the game                                  |
| `main()`           | Controls replaying the game                                          |

---

## Extra Improvements I Added

I improved the project by adding:

- A reusable `get_choice()` function for validated text input
- A reusable `get_guess()` function for validated number input
- Constants for difficulty turns and number range
- A clear game loop that stops immediately when the player wins
- Better messages for invalid input
- `clear_screen()` using the `os` module
- Cleaner function names and type hints
- A cyberpunk-style ASCII logo in `art.py`

---

## Project Structure

```text
012_number_guessing_game/
├── art.py
├── main.py
└── README.md
```

---

## How to Run

From inside the project folder, run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

---

## Example Flow

```text
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Choose difficulty. Type 'easy' or 'hard': hard

You have 5 attempts remaining to guess the number.
Make a guess (1-100): 50
Too low.
Guess again.

You have 4 attempts remaining to guess the number.
Make a guess (1-100): 75
Too high.
Guess again.
```

---

## What I Learned

This project helped me understand that scope matters when organizing a program. Constants like difficulty turns and number ranges should be easy to find and easy to change.

I also learned that input validation makes a small console project feel much more solid. Instead of trusting the user to type the correct thing, the program guides them until the input is usable.

The biggest lesson from this project was that a simple game can still be written in a clean and maintainable way when each function has one clear responsibility.

# Day 11 - Blackjack

This is my solution for **Day 11** of the **100 Days of Code: Python Bootcamp by Angela Yu**.

Day 11 is the first bigger capstone-style project in the beginner section. The goal was to build a playable command-line Blackjack game while combining many of the concepts from the previous days.

I tried to keep the project clean, readable, and more organized by separating the game logic into functions instead of writing everything in one long script.

---

## Project Idea

The game simulates a simplified version of Blackjack.

The player and dealer both receive cards. The player can choose to draw another card or pass. After the player stops, the dealer draws cards until reaching the required score range. The winner is then decided based on who is closer to 21 without going over.

---

## Simplified Rules Used

- Number cards keep their normal value.
- Face cards are represented as `10`.
- Ace starts as `11`.
- If the hand goes over 21 and contains an Ace, the Ace is converted from `11` to `1`.
- A two-card hand that equals 21 is treated as Blackjack.
- The dealer keeps drawing cards while their score is below 17.
- The player loses if their score goes over 21.
- The winner is the hand closest to 21 without busting.

---

## What I Practiced

Through this project, I practiced:

- Breaking a program into clear functions
- Working with lists to store player and dealer cards
- Using loops to control the game flow
- Using conditionals to handle game decisions
- Calculating scores with special Ace logic
- Comparing player and dealer results
- Validating user input
- Clearing the terminal screen using the `os` module
- Keeping the main game loop readable and organized

---

## Functions Used

The project is organized around these main functions:

| Function            | Purpose                                                 |
| ------------------- | ------------------------------------------------------- |
| `clear_screen()`    | Clears the terminal for a cleaner game experience       |
| `get_choice()`      | Validates user input for yes/no choices                 |
| `deal_card()`       | Returns a random card from the deck                     |
| `calculate_score()` | Calculates the current score and handles Ace logic      |
| `decide_winner()`   | Compares the final scores and returns the result        |
| `play_game()`       | Runs one complete round of Blackjack                    |
| `main()`            | Controls whether the player wants to start another game |

---

## Extra Improvements I Added

I tried to improve the project beyond the basic version by adding:

- A reusable input validation function
- Cleaner terminal clearing instead of printing many empty lines
- A cyberpunk-style ASCII logo in `art.py`
- Better function separation
- More readable result messages
- Safer score handling to avoid unbound variable issues
- A more professional project structure

---

## Project Structure

```text
011_blackjack/
├── art.py
├── main.py
└── README.md
```

If I keep extra practice files later, they are only for learning and experimentation. The main game should run from `main.py`.

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
Do you want to play Blackjack? Type 'y' or 'n': y

Your cards: [10, 7], current score: 17
Dealer's first card: 6
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 7], final score: 17
Dealer's final hand: [6, 10, 3], final score: 19
You lose.
```

---

## What I Learned

This project made me think more carefully about how to design a program before coding it.

At first, I only thought about a few functions like `deal_card()` and `decide_winner()`. But while planning the game, I realized that score calculation, input validation, screen clearing, and replay control each deserve their own function.

The biggest lesson from this project was that organizing code into functions is not just about making the file look cleaner. It helps each part of the program have one clear responsibility, which makes the game easier to understand, debug, and improve.

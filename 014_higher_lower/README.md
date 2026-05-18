# Day 14 - Higher Lower Game

This is my solution for **Day 14** of the **100 Days of Code: Python Bootcamp by Angela Yu**.

Day 14 is the **Higher Lower Game Project**. The goal is to compare two public figures, brands, or accounts and guess which one has the higher follower count.

I built the project as a command-line game using separate files for the game logic, ASCII art, and account data.

---

## Project Idea

The game shows two accounts:

- **Compare A**
- **Against B**

The player chooses which account they think has more followers.

If the answer is correct:

- the score increases,
- the winner becomes the next comparison,
- and the game continues.

If the answer is wrong:

- the game ends,
- and the final score is shown.

---

## What I Practiced

Through this project, I practiced:

- Working with dictionaries
- Reading data from a separate file
- Randomly selecting data from a list
- Avoiding duplicate comparisons
- Formatting account data for display
- Comparing hidden values
- Validating user input
- Keeping score
- Reusing the winner as the next comparison
- Organizing a larger beginner project into clear functions

---

## Functions Used

The project is organized around these main functions:

| Function               | Purpose                                                      |
| ---------------------- | ------------------------------------------------------------ |
| `clear_screen()`       | Clears the terminal screen                                   |
| `get_random_account()` | Selects a random account from `game_data.py`                 |
| `format_account()`     | Formats account information without revealing follower count |
| `get_user_choice()`    | Validates whether the user selected A or B                   |
| `has_more_followers()` | Compares follower counts and returns the correct answer      |
| `check_answer()`       | Checks whether the user's choice is correct                  |
| `play_game()`          | Runs the main game loop                                      |
| `main()`               | Controls replaying the game                                  |

---

## Extra Improvements I Added

I improved the project by adding:

- Input validation for A/B choices
- Replay logic after the game ends
- Terminal clearing for a cleaner experience
- A function to avoid comparing the same account twice
- Cleaner function names and type hints
- Separate responsibility for formatting, comparing, checking, and running the game
- A cyberpunk-style ASCII logo in `art.py`

---

## Project Structure

```text
014_higher_lower/
├── art.py
├── game_data.py
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
Compare A: Cristiano Ronaldo, a footballer, from Portugal.

VS

Against B: Instagram, a social media platform, from United States.

Who has more followers? Type 'A' or 'B': B

You're right! Current score: 1.
```

---

## What I Learned

This project helped me practice building a game that depends on structured data.

The main challenge was not just comparing two numbers. It was organizing the flow of the game: selecting random accounts, hiding the follower count, checking the user's answer, keeping the score, and making the winner carry into the next round.

The biggest lesson from this project was that clean structure makes game logic much easier to control.

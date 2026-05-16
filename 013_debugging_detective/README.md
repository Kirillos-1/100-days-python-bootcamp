# Day 13 - Debugging Detective

This is my custom project for **Day 13** of the **100 Days of Code: Python Bootcamp by Angela Yu**.

Day 13 focuses on debugging: learning how to find errors, understand what went wrong, and fix code with a clearer mindset. Since this day does not have a normal final project like the earlier days, I created a small console project based on the same idea.

---

## Project Idea

**Debugging Detective** is a command-line quiz game.

The player is shown small broken Python code snippets. For each case, the player has to identify the type of bug:

- Syntax bug
- Logic bug
- Type bug
- Index bug
- Scope bug

The program gives optional hints, checks the answer, explains the bug, and keeps score until all debugging cases are complete.

---

## What I Practiced

Through this project, I practiced:

- Debugging mindset
- Reading broken code carefully
- Understanding common Python errors
- Differentiating between syntax, logic, type, index, and scope problems
- Lists and dictionaries
- Functions
- Loops
- Input validation
- Score tracking
- Cleaner console project structure

---

## Functions Used

| Function | Purpose |
|---|---|
| `clear_screen()` | Clears the terminal screen |
| `get_choice()` | Validates user input |
| `show_bug_types()` | Displays the available bug categories |
| `run_case()` | Runs one debugging challenge |
| `play_game()` | Runs the full debugging game |
| `main()` | Controls replaying the project |

---

## Project Structure

```text
013_debugging_detective/
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
[1/5] Case 01 - The Silent Total
------------------------------------------------------------
numbers = [10, 20, 30]
total = 0

for number in numbers:
    total + number

print(total)
------------------------------------------------------------

Do you want a hint? Type 'y' or 'n': y
Hint: The code runs, but the total never changes.

What type of bug is this? logic

Correct.
Explanation: The expression `total + number` calculates a value but does not store it.
```

---

## What I Learned

This project helped me treat debugging as a skill, not just a moment of panic when something breaks.

The biggest lesson from Day 13 is that errors become easier to solve when I slow down, read the code carefully, reproduce the problem, and think about what kind of bug I am dealing with.

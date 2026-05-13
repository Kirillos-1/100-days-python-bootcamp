# Day 10 - Calculator

This is my solution for **Day 10** of the **100 Days of Code: Python Bootcamp by Angela Yu**.

The goal of this project was to build a command-line calculator while practicing **functions with outputs**. Instead of only writing the basic version, I tried to make the program cleaner, safer, and more practical to use.

---

## Project Idea

The calculator allows the user to perform basic arithmetic operations:

- Addition
- Subtraction
- Multiplication
- Division

After each calculation, the user can choose to:

- Continue calculating with the previous result
- Start a new calculation
- Quit the program completely

---

## What I Practiced

Through this project, I practiced:

- Writing functions that return values
- Using type hints in Python
- Mapping operators to functions using a dictionary
- Validating user input
- Handling invalid numbers
- Handling invalid operators
- Handling division by zero
- Using loops to control the calculator flow
- Keeping the code organized and readable

---

## Extra Improvements I Added

I tried to make the project feel more like a real small program, not just a simple course exercise.

Some improvements I added:

- A `get_number()` function to keep asking until the user enters a valid number
- A `get_operator()` function to prevent invalid operator choices
- A `get_continue_choice()` function to handle continuing, restarting, or quitting
- Division-by-zero protection using `ZeroDivisionError`
- Cleaner function-based structure instead of putting all logic directly inside the main loop
- Formatted output to make results easier to read

---

## Project Structure

```text
010_calculator/
├── art.py
├── main.py
├── section_code.py
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
What's the first number? 10
Pick an operator:
+
-
*
/
Your choice: +
What's the second number? 5

10.0 + 5.0 = 15.00

Type 'y' to continue calculating with 15.00,
type 'n' to start a new calculation,
or type 'q' to quit:
```

---

## What I Learned

This project helped me understand that functions are not only used to avoid repeating code. They also make the program easier to read, test, debug, and improve later.

The biggest lesson from this day was that clean code is not about making the program look complex. It is about making the logic clear and reliable.

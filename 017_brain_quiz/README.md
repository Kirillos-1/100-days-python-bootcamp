# Day 17 - OOP Quiz Game

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-OOP%20Quiz%20Game-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Concept](https://img.shields.io/badge/Concept-Classes%20%26%20Objects-black?style=for-the-badge)

```text
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                  Q U I Z   B R A I N                         ║
║                 DAY 17 // PYTHON OOP                         ║
║                                                              ║
║        Question objects  →  QuizBrain  →  Score tracking     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

This is my solution for **Day 17** of the **100 Days of Code: Python Bootcamp by Angela Yu**.

Day 17 continues the Object-Oriented Programming part of the course by building a **True / False Quiz Game**. The main idea is to separate the quiz data, the question model, and the quiz logic into different files and objects.

Instead of writing one long script, the project is organized around classes that each have one clear responsibility.

---

## Project Idea

The program asks the user a series of True / False questions.

For each question:

- the question text is shown,
- the user answers `True` or `False`,
- the program checks the answer,
- the score is updated,
- and the quiz continues until there are no questions left.

At the end, the final score is displayed.

---

## Why This Project Matters

This project is small, but it is important because it shows how OOP can make a program easier to control.

The quiz has different parts:

| Part                | Responsibility                                       |
| ------------------- | ---------------------------------------------------- |
| `data.py`           | Stores the raw question data                         |
| `question_model.py` | Defines what a single question is                    |
| `quiz_brain.py`     | Controls question flow, answer checking, and scoring |
| `main.py`           | Builds the question bank and runs the quiz           |
| `art.py`            | Stores the terminal logo                             |

Each file has a purpose, and the logic becomes much easier to understand.

---

## Project Structure

```text
017_quiz_game/
├── art.py
├── data.py
├── main.py
├── question_model.py
├── quiz_brain.py
└── README.md
```

---

## Main Features

- Uses Object-Oriented Programming
- Creates `Question` objects from raw data
- Stores all questions in a question bank
- Uses a `QuizBrain` class to control the quiz
- Tracks question number
- Tracks score
- Checks user answers
- Displays feedback after every answer
- Prints the final score at the end
- Uses a cyberpunk-style terminal logo

---

## Classes Used

### `Question`

Represents one quiz question.

```python
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
```

The `Question` object stores:

- the question text
- the correct answer

---

### `QuizBrain`

Controls the quiz logic.

Typical responsibilities:

- keeping track of the current question number,
- checking if there are still questions left,
- asking the next question,
- checking the user's answer,
- updating the score.

---

## Program Flow

```text
Start program
     |
     v
Load question data
     |
     v
Create Question objects
     |
     v
Store objects in question_bank
     |
     v
Create QuizBrain object
     |
     v
Ask questions while questions remain
     |
     v
Check answer and update score
     |
     v
Print final score
```

---

## What I Practiced

Through this project, I practiced:

- Object-Oriented Programming
- Creating classes
- Creating objects from classes
- Writing constructors using `__init__`
- Working with attributes
- Passing objects into another class
- Building a list of objects
- Separating data from logic
- Controlling program flow through methods
- Score tracking
- Writing cleaner multi-file Python projects

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
Q.1: A slug's blood is green. (True/False): True
You got it right.
The correct answer was: True.
Your current score is: 1/1

Q.2: The loudest animal is the African Elephant. (True/False): False
You got it right.
The correct answer was: False.
Your current score is: 2/2
```

---

## What I Learned

This project helped me understand the value of separating responsibilities.

`Question` does not control the quiz.  
It only stores question data.

`QuizBrain` does not store the raw question database.  
It controls the quiz behavior.

`main.py` does not check answers directly.  
It connects the parts together and runs the program.

The biggest lesson from Day 17 was that OOP is not just about creating classes. It is about deciding what each part of the program should be responsible for.

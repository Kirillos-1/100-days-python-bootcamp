# Day 19 - Turtle Race

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-Turtle%20Race-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Concept](https://img.shields.io/badge/Concept-Turtle%20Instances%20%26%20Randomness-purple?style=for-the-badge)

```text
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                  T U R T L E   R A C E                       ║
║                    DAY 19 // PYTHON                          ║
║                                                              ║
║        multiple turtles → random movement → winner check     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

This is one of my **Day 19** projects from the **100 Days of Code: Python Bootcamp by Angela Yu**.

The project uses Python's **Turtle Graphics** module to create a simple turtle racing game. The user places a bet on one turtle color, then multiple turtle instances race across the screen with random movement. The first turtle to reach the finish line wins.

---

## Project Idea

The program creates six turtle racers:

- Red
- Orange
- Yellow
- Green
- Blue
- Purple

The user chooses a color before the race starts. Then every turtle moves forward by a random distance until one of them reaches the finish line.

At the end, the program prints whether the user's bet was correct.

---

## Main Features

- Creates multiple Turtle objects
- Uses a list to store all turtle racers
- Uses a loop to generate turtles automatically
- Places each turtle at a different starting position
- Takes a user bet with `screen.textinput()`
- Moves turtles by random distances
- Checks each turtle's x-coordinate to detect the winner
- Prints whether the user won or lost

---

## Project Structure

```text
019_turtle_race/
├── main.py
├── section_code.py
└── README.md
```

`main.py` contains the Turtle Race game.  
`section_code.py` contains the Etch-A-Sketch keyboard-control practice project.

---

## How the Program Works

```text
Start screen
     |
     v
Ask user to bet on a turtle color
     |
     v
Create six turtle racers using a loop
     |
     v
Place each turtle at the starting line
     |
     v
Start the race if the bet is valid
     |
     v
Move each turtle forward by a random distance
     |
     v
Check if any turtle reached the finish line
     |
     v
Print win/loss result
```

---

## Important Code Idea

Instead of creating variables manually like:

```python
red_turtle = Turtle()
orange_turtle = Turtle()
yellow_turtle = Turtle()
```

the project creates turtles using a loop and stores them in a list:

```python
all_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
```

This is cleaner because the race logic can loop over all turtles:

```python
for turtle in all_turtles:
    turtle.forward(random.randint(0, 10))
```

---

## What I Practiced

Through this project, I practiced:

- Turtle Graphics
- Creating multiple objects
- Storing objects in a list
- Looping through objects
- User input with `screen.textinput()`
- Random movement
- Checking turtle coordinates with `xcor()`
- Conditional logic
- Simple game flow
- Building an interactive visual program

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

A Turtle window will open, and the program will ask for your bet.

---

## What I Learned

This project made object instances feel more practical.

Each turtle is its own object, but all turtles can be handled together through a list. That made the code much cleaner than trying to create separate variable names for every turtle.

The biggest lesson was that when you need many similar objects, a loop plus a list is usually much better than writing everything manually.

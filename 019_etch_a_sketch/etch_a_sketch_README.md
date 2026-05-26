# Day 19 - Etch-A-Sketch Turtle Controller

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-Etch--A--Sketch-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Concept](https://img.shields.io/badge/Concept-Keyboard%20Events-purple?style=for-the-badge)

```text
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              E T C H - A - S K E T C H                       ║
║                    DAY 19 // PYTHON                          ║
║                                                              ║
║           keyboard events → turtle movement → drawing        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

This is one of my **Day 19** practice projects from the **100 Days of Code: Python Bootcamp by Angela Yu**.

The project uses Python's **Turtle Graphics** module to create a keyboard-controlled drawing program. The turtle moves forward, backward, turns left, turns right, and can clear the drawing using keyboard keys.

---

## Project Idea

This project works like a simple Etch-A-Sketch.

The user controls the turtle with the keyboard:

| Key | Action                                  |
| --- | --------------------------------------- |
| `W` | Move forward                            |
| `S` | Move backward                           |
| `A` | Turn left                               |
| `D` | Turn right                              |
| `C` | Clear drawing and reset turtle position |

The program listens for key presses and calls the correct function whenever a key is pressed.

---

## Project Structure

```text
019_turtle_race/
├── main.py
├── section_code.py
└── README.md
```

`section_code.py` contains the Etch-A-Sketch keyboard-control practice project.

---

## How the Program Works

```text
Create turtle
     |
     v
Create screen
     |
     v
Define movement functions
     |
     v
Start listening for keyboard input
     |
     v
Bind keys to functions
     |
     v
User controls the turtle
     |
     v
Screen closes when clicked
```

---

## Functions Used

| Function          | Purpose                                        |
| ----------------- | ---------------------------------------------- |
| `move_forward()`  | Moves the turtle forward by 10 steps           |
| `move_backward()` | Moves the turtle backward by 10 steps          |
| `turn_right()`    | Rotates the turtle 10 degrees to the right     |
| `turn_left()`     | Rotates the turtle 10 degrees to the left      |
| `clear_screen()`  | Clears the drawing and returns the turtle home |

---

## Important Code Idea

The key part of the project is event binding:

```python
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
```

This tells the screen to listen for keyboard input and call a function when a matching key is pressed.

---

## What I Practiced

Through this project, I practiced:

- Turtle Graphics
- Keyboard events
- Event listeners
- Function callbacks
- Moving a turtle forward and backward
- Rotating a turtle using heading values
- Clearing and resetting the screen
- Writing small focused functions
- Creating an interactive drawing program

---

## How to Run

From inside the project folder, run:

```bash
python section_code.py
```

On some systems, use:

```bash
python3 section_code.py
```

A Turtle window will open. Click inside it if needed, then use `W`, `A`, `S`, `D`, and `C`.

---

## What I Learned

This project introduced event-driven programming in a simple visual way.

Instead of the program running only from top to bottom, it waits for the user to press keys. Each key triggers a different function.

The biggest lesson was understanding that functions can be passed as behavior to event handlers, which makes programs feel interactive instead of static.

# Day 18 - Hirst Dot Painting with Turtle Graphics

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Main%20Project-Hirst%20Dot%20Painting-purple?style=for-the-badge)
![Graphics](https://img.shields.io/badge/Graphics-Turtle-green?style=for-the-badge)
![Library](https://img.shields.io/badge/Library-colorgram.py-orange?style=for-the-badge)

```text
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              H I R S T   D O T   P A I N T I N G             ║
║                  DAY 18 // TURTLE GRAPHICS                   ║
║                                                              ║
║        image palette → RGB colors → dot grid painting        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

This is my **main project for Day 18** of the **100 Days of Code: Python Bootcamp by Angela Yu**.

Day 18 focuses on **Turtle Graphics** and visual programming in Python. The main project is a **Hirst-style dot painting generator**, where the program extracts a color palette from an image and uses Turtle to draw a 10 × 10 grid of randomly colored dots.

I also kept an organized `section_code.py` file for the practice drawings from the lesson, but the main project of the day is the Hirst painting program in `main.py`.

---

## Main Project Idea

The program creates a colorful dot painting using:

- `colorgram.py` to extract colors from an image,
- `turtle` to draw the artwork,
- `random.choice()` to pick colors,
- loops to place dots in a grid,
- and coordinate-style movement to create rows.

The result is a 100-dot painting arranged as a 10 × 10 grid.

---

## Project Files

```text
018_turtle_graphics/
├── hirst_paint.jpg
├── main.py
├── section_code.py
└── README.md
```

| File              | Purpose                                     |
| ----------------- | ------------------------------------------- |
| `main.py`         | Main Hirst-style dot painting project       |
| `hirst_paint.jpg` | Source image used for color extraction      |
| `section_code.py` | Organized practice drawings from the lesson |
| `README.md`       | Project documentation                       |

---

## How the Main Program Works

```text
Start program
     |
     v
Extract 30 colors from hirst_paint.jpg using colorgram
     |
     v
Convert extracted colors into RGB tuples
     |
     v
Move turtle to the starting position
     |
     v
Draw 100 dots in a 10 × 10 grid
     |
     v
Randomly choose a color for each dot
     |
     v
Move to the next row every 10 dots
     |
     v
Wait for screen click to close
```

---

## Main Concepts Practiced

Through the main project, I practiced:

- Turtle Graphics
- Using third-party Python libraries
- Installing and importing external packages
- Extracting colors from an image
- Working with RGB color tuples
- Using `t.colormode(255)`
- Random color selection
- Drawing dots with `tim.dot()`
- Using loops to create a grid
- Controlling turtle movement and direction
- Hiding the turtle for a cleaner final artwork
- Separating practice code from the final project

---

## Main Code Behavior

The project extracts 30 colors:

```python
colors = colorgram.extract("./hirst_paint.jpg", 30)
```

Then it converts each extracted color into an RGB tuple:

```python
new_color = (r, g, b)
rgb_colors.append(new_color)
```

After that, it draws 100 dots:

```python
number_of_dots = 100
```

Every dot uses a random color from the extracted palette:

```python
tim.dot(20, random.choice(rgb_colors))
```

And every 10 dots, the turtle moves up to start a new row.

---

## Practice File: `section_code.py`

The `section_code.py` file contains the organized lesson practice drawings.

It includes:

| Drawing        | Description                                   |
| -------------- | --------------------------------------------- |
| Square         | Basic repeated movement and turning           |
| Dashed Line    | Uses `penup()` and `pendown()`                |
| Polygon Series | Draws shapes from triangle to decagon         |
| Random Walk    | Draws random movement using random colors     |
| Spirograph     | Draws rotated circles into a colorful pattern |

This file is useful because it keeps all the Day 18 drawing experiments in one organized place.

---

## Requirements

This project uses Python's built-in Turtle module and the external `colorgram.py` package.

Install `colorgram.py` with:

```bash
python -m pip install colorgram.py
```

---

## How to Run the Main Project

From inside the project folder, run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

Make sure `hirst_paint.jpg` is in the same folder as `main.py`.

---

## How to Run the Practice File

```bash
python section_code.py
```

This opens a Turtle window and draws the organized practice shapes.

---

## What I Learned

This project made Day 18 feel more creative.

The most important lesson was that programming is not only about logic in the terminal. With Turtle, loops and functions can become something visual.

I also learned how useful external libraries can be. Instead of manually choosing colors, the program extracts a real color palette from an image and uses it to generate the artwork.

The final project helped me connect multiple ideas together:

- image color extraction,
- RGB colors,
- loops,
- Turtle movement,
- and visual design.

That made the Hirst painting feel like the real main project of the day.

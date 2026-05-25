import random
import turtle as t

# ============================================================
# DAY 18 - TURTLE GRAPHICS SECTION CODE
# Organized version of all drawing exercises:
# 1. Square
# 2. Dashed line
# 3. Different polygon shapes
# 4. Random walk
# 5. Spirograph
# ============================================================

# ----------------------------
# Screen setup
# ----------------------------

screen = t.Screen()
screen.setup(width=1200, height=900)
screen.title("Day 18 - Turtle Graphics Practice")

t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")

writer = t.Turtle()
writer.hideturtle()
writer.penup()
writer.speed("fastest")


# ----------------------------
# Helper functions
# ----------------------------

def random_color() -> tuple[int, int, int]:
    """Return a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def move_to(x: int, y: int) -> None:
    """Move the turtle to a position without drawing."""
    tim.penup()
    tim.goto(x, y)
    tim.pendown()


def write_title(text: str, x: int, y: int) -> None:
    """Write a section title on the screen."""
    writer.goto(x, y)
    writer.write(text, align="center", font=("Arial", 14, "bold"))


def reset_turtle_settings() -> None:
    """Reset common turtle drawing settings before each section."""
    tim.pensize(2)
    tim.setheading(0)
    tim.color("black")
    tim.pendown()


# ----------------------------
# Drawing 1: Square
# ----------------------------

def draw_square(side_length: int = 100) -> None:
    """Draw a square."""
    reset_turtle_settings()
    tim.color(random_color())

    for _ in range(4):
        tim.forward(side_length)
        tim.right(90)


# ----------------------------
# Drawing 2: Dashed line
# ----------------------------

def draw_dashed_line(dash_length: int = 10, gap_length: int = 10, number_of_dashes: int = 18) -> None:
    """Draw a dashed line."""
    reset_turtle_settings()
    tim.color(random_color())

    for _ in range(number_of_dashes):
        tim.forward(dash_length)
        tim.penup()
        tim.forward(gap_length)
        tim.pendown()


# ----------------------------
# Drawing 3: Regular polygon
# ----------------------------

def draw_regular_polygon(number_of_sides: int, side_length: int = 55) -> None:
    """Draw one regular polygon based on the number of sides."""
    angle = 360 / number_of_sides

    for _ in range(number_of_sides):
        tim.forward(side_length)
        tim.right(angle)


def draw_polygon_series() -> None:
    """Draw polygons from triangle to decagon."""
    reset_turtle_settings()

    start_x = -520
    start_y = 100
    horizontal_gap = 260
    vertical_gap = 180

    for index, sides in enumerate(range(3, 11)):
        column = index % 4
        row = index // 4

        x = start_x + column * horizontal_gap
        y = start_y - row * vertical_gap

        move_to(x, y)
        tim.setheading(0)
        tim.color(random_color())
        draw_regular_polygon(number_of_sides=sides)

        writer.goto(x + 35, y - 45)
        writer.write(f"{sides} sides", align="center", font=("Arial", 10, "normal"))


# ----------------------------
# Drawing 4: Random walk
# ----------------------------

def draw_random_walk(steps: int = 120, step_length: int = 22) -> None:
    """Draw a random walk."""
    reset_turtle_settings()

    directions = [0, 90, 180, 270]
    tim.pensize(8)

    for _ in range(steps):
        tim.color(random_color())
        tim.forward(step_length)
        tim.setheading(random.choice(directions))


# ----------------------------
# Drawing 5: Spirograph
# ----------------------------

def draw_spirograph(radius: int = 75, size_of_gap: int = 5) -> None:
    """Draw a colorful spirograph."""
    reset_turtle_settings()
    tim.pensize(2)

    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + size_of_gap)


# ----------------------------
# Main drawing controller
# ----------------------------

def draw_all_sections() -> None:
    """Draw every Turtle exercise in an organized way."""

    # Main page title
    write_title("Day 18 - Turtle Graphics Practice", 0, 405)

    # 1. Square
    write_title("1. Square", -420, 340)
    move_to(-470, 300)
    draw_square(side_length=100)

    # 2. Dashed line
    write_title("2. Dashed Line", 250, 340)
    move_to(100, 300)
    draw_dashed_line(dash_length=12, gap_length=12, number_of_dashes=16)

    # 3. Polygon series
    write_title("3. Polygons: Triangle to Decagon", 0, 175)
    draw_polygon_series()

    # 4. Random walk
    write_title("4. Random Walk", -300, -260)
    move_to(-300, -330)
    draw_random_walk(steps=120, step_length=22)

    # 5. Spirograph
    write_title("5. Spirograph", 350, -260)
    move_to(350, -360)
    draw_spirograph(radius=75, size_of_gap=5)

    tim.hideturtle()


# ----------------------------
# Run program
# ----------------------------

draw_all_sections()

screen.exitonclick()
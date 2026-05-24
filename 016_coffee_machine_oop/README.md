# Day 16 - OOP Coffee Machine

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-OOP%20Coffee%20Machine-brown?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Concept](https://img.shields.io/badge/Concept-Object%20Oriented%20Programming-purple?style=for-the-badge)

```text
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              O O P   C O F F E E   M A C H I N E             ║
║                    DAY 16 // PYTHON OOP                      ║
║                                                              ║
║        CoffeeMaker  +  MoneyMachine  +  Menu  +  main        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

This is my solution for **Day 16** of the **100 Days of Code: Python Bootcamp by Angela Yu**.

Day 16 rebuilds the Coffee Machine project using **Object-Oriented Programming**. Instead of keeping everything as separate functions and dictionaries inside one file, the program is now divided into classes with clear responsibilities.

---

## Project Idea

The machine allows the user to order:

- Espresso
- Latte
- Cappuccino

It also supports:

- `report` — prints current machine resources and profit
- `off` — turns off the machine

The user chooses a drink, the machine checks whether enough resources are available, processes payment, deducts ingredients, and serves the drink if everything succeeds.

---

## Why This Version Is Different

Day 15 solved the Coffee Machine using procedural programming.

Day 16 solves the same idea using OOP.

That means the logic is now separated into objects:

| Class | Responsibility |
|---|---|
| `CoffeeMaker` | Stores resources, checks ingredients, and makes coffee |
| `MoneyMachine` | Handles coins, payment, change, and profit |
| `MenuItem` | Models a single drink |
| `Menu` | Stores all drinks and finds the selected drink |
| `main.py` | Controls the program flow |

---

## Project Structure

```text
016_coffee_machine_oop/
├── art.py
├── coffee_maker.py
├── main.py
├── menu.py
├── money_machine.py
├── section_code.py
└── README.md
```

---

## Main Features

- Uses classes and objects
- Separates program responsibilities
- Validates user commands
- Supports drink ordering
- Supports `report` and `off`
- Checks resources before payment
- Processes coins
- Gives change
- Tracks profit
- Deducts ingredients after a successful transaction
- Uses a cyberpunk-style terminal logo

---

## How the Program Works

```text
Start program
     |
     v
Create objects:
CoffeeMaker, MoneyMachine, Menu
     |
     v
Ask user for a command
     |
     |-- off ------> stop program
     |
     |-- report ---> coffee_maker.report()
     |               money_machine.report()
     |
     |-- drink ----> menu.find_drink()
                     |
                     v
              coffee_maker.is_resource_sufficient()
                     |
                     v
              money_machine.make_payment()
                     |
                     v
              coffee_maker.make_coffee()
```

---

## What I Practiced

Through this project, I practiced:

- Object-Oriented Programming
- Creating objects from classes
- Using methods to control object behavior
- Separating responsibilities between classes
- Working with attributes
- Reading and using class-based starter code
- Building a clean controller in `main.py`
- Input validation
- Program flow control
- Improving the same project from procedural style to OOP style

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
What would you like? (latte/espresso/cappuccino): latte

Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0

Here is your latte ☕️. Enjoy!
```

---

## Report Example

```text
What would you like? (latte/espresso/cappuccino): report

========== MACHINE REPORT ==========
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.50
====================================
```

---

## What I Learned

This project helped me understand why OOP is useful.

The goal is not just to use classes because they look professional. The real benefit is that each object owns a specific part of the system.

`CoffeeMaker` does not need to know how coins work.  
`MoneyMachine` does not need to know how much water a latte needs.  
`Menu` does not need to make coffee.  
`main.py` simply coordinates everything.

The biggest lesson from this project was that good object-oriented design makes the program easier to read, extend, and debug.

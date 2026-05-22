# Day 15 - Coffee Machine

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-Coffee%20Machine-brown?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Mode](https://img.shields.io/badge/Mode-Terminal%20App-black?style=for-the-badge)

```text
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ╭──────────────────────────────────────────────────────╮   ║
║   │  N E O N   B R E W   T E R M I N A L                 │   ║
║   │  DAY 15 // COFFEE MACHINE                            │   ║
║   ╰──────────────────────────────────────────────────────╯   ║
║                                                              ║
║        espresso  |  latte  |  cappuccino  |  report  | off   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

This is my solution for **Day 15** of the **100 Days of Code: Python Bootcamp by Angela Yu**.

Day 15 is the **Coffee Machine Program**. The goal is to build a command-line coffee machine that can take orders, check resources, process coins, return change, update profit, deduct ingredients, and keep serving customers until the maintainer turns it off.

I built this project with a clean function-based structure instead of putting all the logic in one long loop.

---

## Project Idea

The coffee machine supports three drinks:

- Espresso
- Latte
- Cappuccino

It also supports two special commands:

- `report` — shows the current resources and money
- `off` — turns off the machine

The machine keeps running until the user enters `off`.

---

## Main Features

- Validates user drink choices
- Handles `report` and `off` commands
- Checks if enough resources exist before taking money
- Processes coin input
- Rejects invalid coin values
- Refunds money if the user does not insert enough
- Returns change when the user pays too much
- Adds drink cost to machine profit
- Deducts ingredients after a successful transaction
- Serves the selected drink
- Uses a cyberpunk-style terminal logo

---

## Drink Menu

| Drink      | Water |  Milk | Coffee |  Cost |
| ---------- | ----: | ----: | -----: | ----: |
| Espresso   |  50ml |   0ml |    18g | $1.50 |
| Latte      | 200ml | 150ml |    24g | $2.50 |
| Cappuccino | 250ml | 100ml |    24g | $3.00 |

---

## Starting Resources

| Resource | Amount |
| -------- | -----: |
| Water    |  300ml |
| Milk     |  200ml |
| Coffee   |   100g |
| Money    |  $0.00 |

---

## What I Practiced

Through this project, I practiced:

- Working with dictionaries
- Accessing nested dictionary data
- Creating constants
- Writing reusable helper functions
- Validating text input
- Validating numeric input
- Processing money calculations
- Rounding floating-point money values
- Checking resources before continuing an operation
- Updating program state
- Building a loop-based command-line application
- Separating responsibilities between functions

---

## Functions Used

| Function              | Purpose                                          |
| --------------------- | ------------------------------------------------ |
| `clear_screen()`      | Clears the terminal screen                       |
| `get_user_choice()`   | Gets and validates the user's command            |
| `print_report()`      | Prints current resources and money               |
| `check_resources()`   | Checks if the selected drink can be made         |
| `get_coin_count()`    | Gets a valid number of coins from the user       |
| `process_coins()`     | Calculates the total inserted money              |
| `check_transaction()` | Checks payment, gives change, and updates profit |
| `make_coffee()`       | Deducts ingredients and serves the drink         |
| `serve_drink()`       | Runs the full drink-order process                |
| `main()`              | Runs the coffee machine loop                     |

---

## Project Structure

```text
015_coffee_machine/
├── art.py
├── data.py
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
What would you like? (espresso/latte/cappuccino): latte

Please insert coins.

How many quarters: 10
How many dimes: 0
How many nickels: 0
How many pennies: 0

Here is your latte. Enjoy!
```

---

## Report Example

```text
What would you like? (espresso/latte/cappuccino): report

=================== REPORT ===================
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.50
==============================================
```

---

## Program Flow

```text
Start machine
     |
     v
Ask user for command
     |
     |-- off ------> stop program
     |
     |-- report ---> print resources
     |
     |-- drink ----> check resources
                      |
                      |-- not enough ---> cancel order
                      |
                      |-- enough ------> process coins
                                         |
                                         |-- not enough money ---> refund
                                         |
                                         |-- enough money ------> give change if needed
                                                               -> add profit
                                                               -> deduct ingredients
                                                               -> serve drink
```

---

## What I Learned

This project felt like a step up because it is not just a game anymore. It behaves more like a small real-world system.

The biggest lesson was learning how to control the order of operations:

1. Check the machine has enough ingredients.
2. Take money only if the drink can be made.
3. Confirm the transaction.
4. Update money.
5. Deduct ingredients.
6. Serve the drink.

That order matters. If the logic is written in the wrong order, the machine could take money without serving coffee or deduct resources before payment succeeds.

This project helped me see why clean structure matters even in small programs.

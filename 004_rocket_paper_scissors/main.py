import random
import ascii_art

print(ascii_art.logo + "\n")

# Getting choices
user_choice = int(input("What do you want to choose?\n"
                        "0 -> Rock (Shield)\n"
                        "1 -> Paper (Dragon)\n"
                        "2 -> Scissors (Sword)\n"))
computer_choice = random.randint(0, 2)

# Displaying the choices
print(f"User's choice: \n{ascii_art.choices[user_choice]}")
print(f"Computer's choice: \n{ascii_art.choices[computer_choice]}")

# Game logic
if (user_choice == computer_choice):
    print(ascii_art.draw_logo)
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
            print(ascii_art.win_logo)
else:
    print(ascii_art.lose_logo)
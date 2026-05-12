# number = int(input("What is the number you want to check? "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

print("Welcome to the rollercoaster!\n")

height = float(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster.")
    
    bill = 0
    
    age = int(input("What is your age? "))
    if age < 12:
        bill += 5
    elif age <= 18:
        bill += 7
    elif 45 <= age <= 55:
        print("Everything is going to be okay. Have a free ride on us!")
    else:
        bill += 12
        
    photo_take = input("Do you want to have a photo take? Type y for Yes and n for No: ").strip().lower()
    if photo_take == "y":
        bill += 3
        
    print(f"\nYour bill is going to be ${bill:.1f}")
else:
    print("Sorry, you have to grow taller before you can ride.")

# print("Welcome to Python Pizza Deliveries!\n")

# size = input("What size pizza do you want? S, M or L: ").lower()
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
# extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

# bill = 0

# if size == "s":
#     bill += 15
# elif size == "m":
#     bill += 20
# else:
#     bill += 25

# if pepperoni == "y":
#     if size == "s":
#         bill += 2
#     else:
#         bill += 3
        
# if extra_cheese == "y":
#     bill += 1
    
# print(f"\nYour final bill is ${bill}")
    

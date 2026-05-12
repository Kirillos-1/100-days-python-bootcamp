print("""
   ███████╗██████╗  █████╗  ██████╗███████╗
   ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝
   ███████╗██████╔╝███████║██║     █████╗  
   ╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝  
   ███████║██║     ██║  ██║╚██████╗███████╗
   ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝

        🚀 SPACE STATION OMEGA 🚀
""")

print("Mission: Escape before the station explodes 💥")
print("Choose wisely... or drift forever in space.")

choice1 = input(
    "\nYou wake up in the command center.\n"
    "There are two corridors.\n"
    "Do you go LEFT to engineering or RIGHT to the dark tunnel?\n"
).lower()

if choice1 == "right":
    print("\nYou walk into the dark tunnel...")
    print("Suddenly — WHOOSH!")
    print("An airlock opens and sucks you into space.")
    print("💀 You are now officially space dust.")
    print("Game Over 😂")
elif choice1 == "left":
    print("\nYou enter engineering.")
    print("You see a broken bridge leading to escape pods.")
    
    choice2 = input(
        "\nThe bridge looks unstable.\n"
        "Do you WAIT for repair drones or RUN across?\n"
    ).lower()
    
    if choice2 == "run":
        print("\nYou sprint dramatically...")
        print("The bridge collapses.")
        print("You fall into the reactor.")
        print("💀 You are now glowing slightly.")
        print("Game Over 😂")
    elif choice2 == "wait":
        print("\nRepair drones fix the bridge.")
        print("You safely cross to the escape pod bay.")
        
        choice3 = input(
            "\nThere are three escape pods:\n"
            "RED 🔴\n"
            "BLUE 🔵\n"
            "GREEN 🟢\n"
            "Which one do you choose?\n"
        ).lower()
        
        if choice3 == "red":
            print("\nYou enter the red pod...")
            print("It launches instantly!")
            print("Then explodes like popcorn 🍿💥")
            print("💀 Game Over.")
        elif choice3 == "blue":
            print("\nYou launch into deep space...")
            print("Fuel level: 0%")
            print("You slowly drift forever.")
            print("💀 Space is very quiet.")
            print("Game Over.")
        elif choice3 == "green":
            print("\nEngines online.")
            print("Navigation stable.")
            print("You escape safely!")
            print("🏆 Mission Success!")
        elif choice3 == "yellow":
            print("\n🚨 SECRET POD ACTIVATED 🚨")
            print("You discovered the experimental warp pod.")
            print("It teleports you instantly to Earth.")
            print("🏆 SECRET ENDING UNLOCKED!")
        else:
            print("\nYou entered the wrong pod.")
            print("Security lasers activate.")
            print("💀 Zap! Game Over.")
    else:
        print("\nYou waited too long.")
        print("The station exploded 💥")
        print("Game Over.")

else:
    print("\nYou tripped over a cable.")
    print("A robot laughs at you 🤖😂")
    print("💀 Game Over.") 
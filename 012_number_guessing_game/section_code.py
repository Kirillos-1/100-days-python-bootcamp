enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies outside function: {enemies}")


# Global constants - Naming conventions (uppercase)
PI = 3.14159
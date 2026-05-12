def greet():
    print("Hello!")
    print("How do you do?")
    

def greet_with_name_city(name: str="User", city: str="Nowhere") -> None:
    print("Hello,", name)
    print("How is the weather in?", city)


greet()
greet_with_name_city("Kiro", "LA")  # positional argument
greet_with_name_city()
greet_with_name_city(city="Rome", name="Kirillos")  # keyword argument
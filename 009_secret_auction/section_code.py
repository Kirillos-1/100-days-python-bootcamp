programming_dictionary = {
    "Bug": "An error in the program from running as expected.",
    "Function": "A piece of code that you can call easily over and over."
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

programming_dictionary = {}
print(programming_dictionary)

programming_dictionary = {
    "Bug": "An error in the program from running as expected.",
    "Function": "A piece of code that you can call easily over and over."
}
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

print()

for thing in programming_dictionary:
    print(thing)
    
print()

for thing in programming_dictionary:
    print(programming_dictionary[thing])
    
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dihon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
print(travel_log["Germany"][2])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visities": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}
print(travel_log["France"]["cities_visited"][1])
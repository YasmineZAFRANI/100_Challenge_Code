"""
Day 1 project:
Description:
    1-Create a greeting for your program
    2-Ask the user for the city they grew uo in and store it in a variable.
    3-Ask the user for the name of a pet and store it in a variable.
    4-Combine the name of their city and pet and show them their brand name
"""
"""### First try
print("Welcome to the brand name generator.")
city=input("What's the name of the city you grew up in ?\n")
pet=input("What's your pet's name?\n")
print("Your brand name could be:"+ city +" "+pet)

### Version 2
#### strip() to remove accidental spaces and some better formatting + input validation.

# Greeting
print("Welcome to the Brand Name Generator!\n")

# User input
city = input("What's the name of the city you grew up in? ").strip()
pet = input("What's your pet's name? ").strip()

# Ensure inputs are not empty
if not city or not pet:
    print("Oops! You need to enter both a city and a pet name.")
else:
    # Generate and display the brand name
    brand_name = f"{city.capitalize()} {pet.capitalize()}"
    print(f"\nYour brand name could be: {brand_name} 🎉")
    """
###Version 3
import random

# Greeting
greetings = ["Let's create something radom!", "Your future brand starts here!", "Ready to find your brand name?"]
print(random.choice(greetings) + "\n")

# Get user input
city = input("What's the name of the city you grew up in? ").strip()
pet = input("What's your pet's name? ").strip()

# Ensure inputs are not empty
if not city or not pet:
    print("Please provide both your city and pet name.")
else:
    # Create a cool, sleek brand name
    suffixes = ["Labs", "Studio", "Co", "Collective", "Inc", "Works"]
    brand_name = f"{city.capitalize()} {pet.capitalize()} {random.choice(suffixes)}"

    # Show the brand name
    print(f"\nYour brand name could be: {brand_name} 🎉")

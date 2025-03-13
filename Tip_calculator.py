#Split and tip calculator
#Version  1
"""
# Greeting
print("Welcome to the tip calculator!\n")

# User input
Sum_bill = float(input("What was the total bill ? "))
Tip = int(input("What percentage tip would you like to give? 10 12 15 "))
Split = int(input("How many people to split the bill ?"))
#Calculate + print
pay = Sum_bill*(1+ Tip/100)/Split
final_pay=round(pay,2)
print(f"Each person should pay:  {final_pay}\n")
"""
### Revue des inputs + error message
# Tip Calculator

print("Welcome to the Tip Calculator!\n")

# User input with validation
while True:
    try:
        bill = float(input("What was the total bill? €"))
        if bill < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive amount.")

while True:
    try:
        tip = float(input("What percentage tip would you like to give? (e.g., 10, 12.5, 20): "))
        if tip < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid tip percentage (0 or more).")

while True:
    try:
        people = int(input("How many people to split the bill? "))
        if people <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid number of people (at least 1).")

# Calculation
total_per_person = (bill * (1 + tip / 100)) / people

# Display result with two decimal places
print(f"\nEach person should pay: €{total_per_person:.2f}")




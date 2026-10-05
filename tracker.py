# Project: Expense Tracker

# Installment: 1

# Author: Aris Clyde D. Solijon

# A personal expense tracker landing page

# Header

print("=" * 40)
print(" EXPENSE TRACKER")
print(" Know where your money goes.")
print("=" * 40)

print("MAIN MENU")
print(f"{'[1] Add an expense':<25}(coming soon)")
print(f"{'[2] View all expenses':<25}(coming soon)")
print(f"{'[3] Show total spent':<25}(coming soon)")
print(f"{'[4] Exit':<25}(coming soon)")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("-" * 40)
print("SUMMARY")
print(f" - {item1}: ${amount1}")
print(f" - {item2}: ${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)

print("Made by: Aris Clyde D. Solijon | Installment 2")

# Dice Simulator Using Random Module

import random

while True:
    print("\n1. Roll One Die")
    print("2. Roll Two Dice")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = random.randint(1, 6)
        print("Dice result:", result)

    elif choice == "2":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        print("First die:", die1)
        print("Second die:", die2)
        print("Total:", die1 + die2)

    elif choice == "3":
        print("Dice simulation ended.")
        break

    else:
        print("Invalid choice.")

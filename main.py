import random

def dice_rolling():
    # Create a loop that will continue to run until the user says no
    sides = int(input("Number of sides to the die?"))
    while True:
        # Ask the user if they would like to roll the dice
        intro = input("Would you like to roll the dice? (yes/no) ").lower()
        if intro == 'yes':
            # Generate a random number between 1 and 6
            num = random.randint(1, sides)
            print(f"You rolled a {num}")
        elif intro == 'no':
            print("Game over!")
            break
        # If the user enters anything other than yes or no, ask them to try again
        else:
            print("Invalid input. Please try again.")
            continue

dice_rolling()
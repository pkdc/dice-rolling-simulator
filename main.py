import random

def dice_rolling():
    # Create a loop until the user enters a valid number of sides for the die to roll
    sides = -1
    while sides < 0:
        try:
            sides = int(input("Please enter the number of sides to the die (1 or more) or enter 0 to exit: "))
        except ValueError:
            print("Please enter an integer greater than 1 for the number of sides to the die, or 0 to exit.")
    if sides == 0:
        print("You have chosen to exit, goodbye!")
        return
    # Create a loop that will continue to run until the user says no to further dice rolls
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
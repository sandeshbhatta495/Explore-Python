import random  # To generate a random number

# Function to play the guessing game
def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Welcome message
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    # Loop to let the player keep guessing until they get it right
    while True:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        
        # If the guess is less than the number
        if guess < number_to_guess:
            print("Too low! Try again.")
        
        # If the guess is greater than the number
        elif guess > number_to_guess:
            print("Too high! Try again.")
        
        # If the guess is correct
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            break  # Exit the loop when the guess is correct

# Start the game
number_guessing_game()

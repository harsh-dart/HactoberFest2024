import random

def guess_the_number():
    """A simple number guessing game where the player has 7 attempts to guess a randomly generated number between 1 and 100."""
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    
    # Generate a random number
    random_number = random.randint(lower_bound, upper_bound)
    
    # Set the number of attempts
    attempts = 7
    print(f"Guess the number between {lower_bound} and {upper_bound}. You have {attempts} attempts.")

    for attempt_number in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt_number}: Enter your guess: "))
            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
                continue  # Just skip to the next attempt
            
            # Check if the guess is correct
            if guess == random_number:
                print(f"Congratulations! You guessed the correct number {random_number} in {attempt_number} attempts!")
                break
            elif guess < random_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        
        except ValueError:
            print("Please enter a valid number.")
        
        if attempt_number == attempts:
            print(f"Sorry, you've used all {attempts} attempts. The correct number was {random_number}. Better luck next time!")

# Start the game
guess_the_number()

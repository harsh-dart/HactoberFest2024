import random

# Function to roll a die
def roll_dice():
    return random.randint(1, 6)

# Function to simulate a dice game
def dice_game():
    # Player 1 rolls the dice
    player1_roll = roll_dice()
    print(f"Player 1 rolled: {player1_roll}")

    # Player 2 rolls the dice
    player2_roll = roll_dice()
    print(f"Player 2 rolled: {player2_roll}")

    # Determine the winner
    if player1_roll > player2_roll:
        print("Player 1 wins!")
    elif player2_roll > player1_roll:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Start the dice game
dice_game()

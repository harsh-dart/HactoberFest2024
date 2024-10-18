import random

def roll_dice():
    """Simulates rolling a dice, returns a number between 1 and 6."""
    return random.randint(1, 6)

def play_dice_game():
    print("Welcome to the Dice Game!")
    print("Two players will roll a dice. The player with the higher roll wins.")

    # Player 1's turn
    player1_roll = roll_dice()
    print(f"Player 1 rolls: {player1_roll}")

    # Player 2's turn
    player2_roll = roll_dice()
    print(f"Player 2 rolls: {player2_roll}")

    # Determine the winner
    if player1_roll > player2_roll:
        print("Player 1 wins!")
    elif player2_roll > player1_roll:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    play_dice_game()

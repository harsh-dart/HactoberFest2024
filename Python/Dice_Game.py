import random

def roll_dice():
    """Simulate rolling a six-sided die."""
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Game!")
    
    # Player names
    player1 = input("Enter the name of Player 1: ")
    player2 = input("Enter the name of Player 2: ")

    # Roll the dice for both players
    print(f"\n{player1} is rolling the dice...")
    player1_roll = roll_dice()
    print(f"{player1} rolled a {player1_roll}")

    print(f"\n{player2} is rolling the dice...")
    player2_roll = roll_dice()
    print(f"{player2} rolled a {player2_roll}")

    # Determine the winner
    if player1_roll > player2_roll:
        print(f"\n{player1} wins!")
    elif player2_roll > player1_roll:
        print(f"\n{player2} wins!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    play_game()

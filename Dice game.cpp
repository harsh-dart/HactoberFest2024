#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

// Function to roll a dice
int rollDice() {
    return (rand() % 6) + 1; // Generate a random number between 1 and 6
}

// Function to play the game
void playGame() {
    int player1Score = 0;
    int player2Score = 0;

    cout << "Welcome to the Dice Game!" << endl;
    cout << "Player 1 and Player 2 will take turns rolling a dice." << endl;
    cout << "The player with the higher number wins the round." << endl;

    for (int i = 1; i <= 5; i++) {
        cout << "\nRound " << i << ":" << endl;

        // Player 1's turn
        cout << "Player 1 rolls the dice..." << endl;
        int player1Roll = rollDice();
        cout << "Player 1 rolled a " << player1Roll << endl;

        // Player 2's turn
        cout << "Player 2 rolls the dice..." << endl;
        int player2Roll = rollDice();
        cout << "Player 2 rolled a " << player2Roll << endl;

        // Determine the winner of the round
        if (player1Roll > player2Roll) {
            cout << "Player 1 wins this round!" << endl;
            player1Score++;
        } else if (player2Roll > player1Roll) {
            cout << "Player 2 wins this round!" << endl;
            player2Score++;
        } else {
            cout << "It's a tie!" << endl;
        }

        cout << "Score - Player 1: " << player1Score << ", Player 2: " << player2Score << endl;
    }

    // Determine the overall winner
    if (player1Score > player2Score) {
        cout << "\nPlayer 1 wins the game!" << endl;
    } else if (player2Score > player1Score) {
        cout << "\nPlayer 2 wins the game!" << endl;
    } else {
        cout << "\nIt's a tie game!" << endl;
    }
}

int main() {
    srand(time(0)); // Seed the random number generator

    playGame();

    return 0;
}

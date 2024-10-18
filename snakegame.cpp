#include <iostream>
#include <conio.h> // For _kbhit() and _getch()
#include <windows.h> // For Sleep()
#include <vector>
#include <cstdlib> // For rand() and srand()
#include <ctime> // For time()

using namespace std;

// Define the dimensions of the game area
const int WIDTH = 20;
const int HEIGHT = 20;

// Define the direction for the snake
enum Direction { STOP = 0, LEFT, RIGHT, UP, DOWN };

// Struct to represent the snake
struct Snake {
    vector<pair<int, int>> body;
    Direction dir;
    int score;
};

// Function to initialize the game
void Setup(Snake &snake, pair<int, int> &fruit) {
    snake.body.push_back({WIDTH / 2, HEIGHT / 2}); // Initialize snake at the center
    snake.dir = STOP;
    snake.score = 0;
    fruit = {rand() % WIDTH, rand() % HEIGHT}; // Random fruit position
}

// Function to draw the game area
void Draw(Snake &snake, pair<int, int> &fruit) {
    system("cls"); // Clear the console
    for (int y = 0; y < HEIGHT + 2; ++y) {
        for (int x = 0; x < WIDTH + 2; ++x) {
            if (x == 0 || x == WIDTH + 1 || y == 0 || y == HEIGHT + 1) {
                cout << "#"; // Draw the walls
            } else if (x == fruit.first && y == fruit.second) {
                cout << "F"; // Draw the fruit
            } else {
                bool printSnake = false;
                for (auto segment : snake.body) {
                    if (segment.first == x && segment.second == y) {
                        cout << "O"; // Draw the snake
                        printSnake = true;
                        break;
                    }
                }
                if (!printSnake) {
                    cout << " "; // Empty space
                }
            }
        }
        cout << endl;
    }
    cout << "Score: " << snake.score << endl;
}

// Function to input the direction
void Input(Snake &snake) {
    if (_kbhit()) {
        switch (_getch()) {
            case 'a': // Left
                if (snake.dir != RIGHT) snake.dir = LEFT;
                break;
            case 'd': // Right
                if (snake.dir != LEFT) snake.dir = RIGHT;
                break;
            case 'w': // Up
                if (snake.dir != DOWN) snake.dir = UP;
                break;
            case 's': // Down
                if (snake.dir != UP) snake.dir = DOWN;
                break;
            case 'x': // Quit
                snake.dir = STOP;
                break;
        }
    }
}

// Function to update the snake's position
void Logic(Snake &snake, pair<int, int> &fruit) {
    // Get the current head position
    pair<int, int> head = snake.body.front();
    switch (snake.dir) {
        case LEFT: head.first--; break;
        case RIGHT: head.first++; break;
        case UP: head.second--; break;
        case DOWN: head.second++; break;
        default: break;
    }

    // Check for fruit collision
    if (head == fruit) {
        snake.score++;
        snake.body.push_back(fruit); // Add a segment to the snake
        fruit = {rand() % WIDTH, rand() % HEIGHT}; // Generate new fruit
    } else {
        // Move the snake
        snake.body.insert(snake.body.begin(), head);
        snake.body.pop_back(); // Remove the last segment
    }

    // Check for collision with walls or itself
    if (head.first < 1 || head.first > WIDTH || head.second < 1 || head.second > HEIGHT) {
        snake.dir = STOP; // Stop the game if it hits the wall
    }
    for (size_t i = 1; i < snake.body.size(); ++i) {
        if (head == snake.body[i]) {
            snake.dir = STOP; // Stop the game if it collides with itself
        }
    }
}

// Main function to run the game
int main() {
    srand(time(0)); // Seed for random number generation
    Snake snake;
    pair<int, int> fruit;

    Setup(snake, fruit);

    while (snake.dir != STOP) {
        Draw(snake, fruit);
        Input(snake);
        Logic(snake, fruit);
        Sleep(100); // Control the speed of the game
    }

    cout << "Game Over! Your final score was: " << snake.score << endl;
    return 0;
}

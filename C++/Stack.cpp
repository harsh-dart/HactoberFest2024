#include <iostream>
using namespace std;

#define MAX 1000 // Maximum size of the stack

class Stack {
    int top;

public:
    int arr[MAX]; // Array to store stack elements

    Stack() { top = -1; } // Constructor to initialize top as -1

    // Function to push an element onto the stack
    bool push(int x) {
        if (top >= (MAX - 1)) {
            cout << "Stack Overflow" << endl;
            return false;
        } else {
            arr[++top] = x;
            cout << x << " pushed onto stack" << endl;
            return true;
        }
    }

    // Function to remove the top element from the stack
    int pop() {
        if (top < 0) {
            cout << "Stack Underflow" << endl;
            return 0;
        } else {
            int x = arr[top--];
            cout << x << " popped from stack" << endl;
            return x;
        }
    }

    // Function to return the top element without removing it
    int peek() {
        if (top < 0) {
            cout << "Stack is Empty" << endl;
            return 0;
        } else {
            int x = arr[top];
            cout << "Top element is: " << x << endl;
            return x;
        }
    }

    // Function to check if the stack is empty
    bool isEmpty() {
        return (top < 0);
    }
};

int main() {
    Stack stack;
    int choice, value;

    while (true) {
        cout << "\nChoose an operation:\n";
        cout << "1. Push\n";
        cout << "2. Pop\n";
        cout << "3. Peek\n";
        cout << "4. Check if empty\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1: // Push
            cout << "Enter value to push: ";
            cin >> value;
            stack.push(value);
            break;

        case 2: // Pop
            stack.pop();
            break;

        case 3: // Peek
            stack.peek();
            break;

        case 4: // Check if empty
            if (stack.isEmpty()) {
                cout << "Stack is empty" << endl;
            } else {
                cout << "Stack is not empty" << endl;
            }
            break;

        case 5: // Exit
            cout << "Exiting..." << endl;
            return 0;

        default:
            cout << "Invalid choice! Please choose again." << endl;
        }
    }
    return 0;
}

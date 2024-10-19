#include <iostream>
#define MAX 100 

class Stack {
private:
    int arr[MAX]; 
    int top;      
public:
    
    Stack() {
        top = -1;
    }

    
    bool isEmpty() {
        return top == -1;
    }

    bool isFull() {
        return top == MAX - 1;
    }

    void push(int value) {
        if (isFull()) {
            std::cout << "Stack overflow! Cannot push " << value << "\n";
            return;
        }
        arr[++top] = value;
        std::cout << value << " pushed to stack\n";
    }
    int pop() {
        if (isEmpty()) {
            std::cout << "Stack underflow! Cannot pop\n";
            return -1;
        }
        return arr[top--];
    }
    int peek() {
        if (isEmpty()) {
            std::cout << "Stack is empty\n";
            return -1;
        }
        return arr[top];
    }
    void display() {
        if (isEmpty()) {
            std::cout << "Stack is empty\n";
            return;
        }
        std::cout << "Stack elements: ";
        for (int i = 0; i <= top; i++) {
            std::cout << arr[i] << " ";
        }
        std::cout << "\n";
    }
};

int main() {
    Stack stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);

    stack.display();

    std::cout << stack.pop() << " popped from stack\n";

    stack.display();

    std::cout << "Top element is " << stack.peek() << "\n";

    return 0;
}

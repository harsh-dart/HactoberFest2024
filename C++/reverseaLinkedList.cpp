#include <iostream>
using namespace std;

// Node class definition
class Node {
public:
    int data;   // Data held in the node
    Node* next; // Pointer to the next node

    // Constructor to initialize data and next pointer
    Node(int data1) : data(data1), next(nullptr) {}
};

// Function to reverse the linked list
Node* reverseLinkedList(Node* head) {
    Node* temp = head;   // Pointer for traversing the list
    Node* prev = nullptr; // Pointer to keep track of the previous node

    while (temp != nullptr) {
        Node* front = temp->next; // Store the next node
        temp->next = prev;         // Reverse the link
        prev = temp;               // Move prev to current node
        temp = front;              // Move to the next node
    }

    return prev; // New head of the reversed list
}

// Function to print the linked list
void printLinkedList(Node* head) {
    Node* temp = head; // Pointer for traversing the list
    while (temp != nullptr) {
        cout << temp->data << " "; // Print node data
        temp = temp->next;         // Move to the next node
    }
    cout << endl;
}

// Function to free the memory allocated for the linked list
void freeLinkedList(Node* head) {
    Node* temp;
    while (head != nullptr) {
        temp = head;
        head = head->next;
        delete temp; // Free the memory
    }
}

int main() {
    // Create a linked list: 1 -> 3 -> 2 -> 4
    Node* head = new Node(1);
    head->next = new Node(3);
    head->next->next = new Node(2);
    head->next->next->next = new Node(4);

    cout << "Original Linked List: ";
    printLinkedList(head); // Print original list

    head = reverseLinkedList(head); // Reverse the linked list

    cout << "Reversed Linked List: ";
    printLinkedList(head); // Print reversed list

    freeLinkedList(head); // Free allocated memory
    return 0;
}

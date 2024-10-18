#include <iostream>
using namespace std;

class Node {
public:
    int data;   
    Node* next;      

    // Constructor with two parameters
    Node(int data1, Node* next1) {
        data = data1;
        next = next1;
    }

    // Constructor with one parameter (next defaults to nullptr)
    Node(int data1) {
        data = data1;
        next = nullptr;
    }
};

// Function to reverse the linked list
Node* reverseLinkedList(Node *head) {
    Node* temp = head;  
    Node* prev = nullptr;  // Initializing the previous pointer to null

    while (temp != nullptr) {  
        Node* front = temp->next;  // Save the next node
        temp->next = prev;  // Reverse the link
        prev = temp;  // Move prev one step ahead
        temp = front;  // Move temp one step ahead
    }
    return prev;  // prev will be the new head after reversal
}

// Function to print the linked list
void printLinkedList(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " ";  // Print the current node's data
        temp = temp->next;  // Move to the next node
    }
    cout << endl;
}

int main() {
    // Creating a linked list: 1 -> 3 -> 2 -> 4
    Node* head = new Node(1);
    head->next = new Node(3);
    head->next->next = new Node(2);
    head->next->next->next = new Node(4);

    // Print the original linked list
    cout << "Original Linked List: ";
    printLinkedList(head);

    // Reverse the linked list
    head = reverseLinkedList(head);

    // Print the reversed linked list
    cout << "Reversed Linked List: ";
    printLinkedList(head);

    return 0;
}

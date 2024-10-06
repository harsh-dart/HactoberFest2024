/* The main idea is to reverse the linked list, we try to changes the direction of the arrows or links. This in-place reversal allows us to efficiently transform the original list without using extra space.

1. At first we keep a pointer let's say "prev" before the start pointer pointing to null . A temporary node points to first node, a front pointer pointing to the first node itself

2. Now we move forward using a while loop and along the way we point front to the current (temp) pointer's next.

3. Then we point current pointers to the previous pointer which is pointing to null.

4. Then we update previous pointer as the current pointer.

5. Then we update current pointer or temp to the front node.

And voilah! we've reversed a linked list inplace without using any extra space

*/
class Node {
public:
    

    int data;   
    
    Node* next;      

    
    Node(int data1, Node* next1) {
        data = data1;
        next = next1;
    }

    
    Node(int data1) {
        data = data1;
        next = nullptr;
    }
};


Node* reverseLinkedList(Node *head)
{
   
   Node* temp = head;  
   
   Node* prev = NULL;  
   
   
   while(temp != NULL){  
       
       Node* front = temp->next;  
       
       temp->next = prev;  
       
       prev = temp;  
       
       temp = front; 
   }
   
  
   return prev;  
}

// Function to print the linked list
void printLinkedList(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main() {
   
    Node* head = new Node(1);
    head->next = new Node(3);
    head->next->next = new Node(2);
    head->next->next->next = new Node(4);

  
    cout << "Original Linked List: ";
    printLinkedList(head);

 
    head = reverseLinkedList(head);

    cout << "Reversed Linked List: ";
    printLinkedList(head);

    return 0;
}

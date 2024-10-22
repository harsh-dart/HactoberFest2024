#include <stdio.h>

// Function to display the array
void display(int arr[], int n) {
    printf("Array elements: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to insert an element at a given index
void insert(int arr[], int *n, int element, int index) {
    if (index >= 0 && index <= *n) {
        for (int i = *n; i > index; i--) {
            arr[i] = arr[i - 1];
        }
        arr[index] = element;
        (*n)++;
        printf("Inserted %d at index %d\n", element, index);
    } else {
        printf("Invalid index\n");
    }
}

// Function to delete an element at a given index
void delete(int arr[], int *n, int index) {
    if (index >= 0 && index < *n) {
        printf("Deleted %d from index %d\n", arr[index], index);
        for (int i = index; i < *n - 1; i++) {
            arr[i] = arr[i + 1];
        }
        (*n)--;
    } else {
        printf("Invalid index\n");
    }
}

// Function to update an element at a given index
void update(int arr[], int n, int element, int index) {
    if (index >= 0 && index < n) {
        printf("Updated index %d from %d to %d\n", index, arr[index], element);
        arr[index] = element;
    } else {
        printf("Invalid index\n");
    }
}

int main() {
    int arr[100];
    int n = 0; // Number of elements in the array
    int choice, element, index;

    do {
        printf("\nMenu:\n");
        printf("1. Insert\n");
        printf("2. Delete\n");
        printf("3. Update\n");
        printf("4. Display\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter element to insert: ");
                scanf("%d", &element);
                printf("Enter index to insert at: ");
                scanf("%d", &index);
                insert(arr, &n, element, index);
                break;
            case 2:
                printf("Enter index to delete from: ");
                scanf("%d", &index);
                delete(arr, &n, index);
                break;
            case 3:
                printf("Enter new element to update: ");
                scanf("%d", &element);
                printf("Enter index to update at: ");
                scanf("%d", &index);
                update(arr, n, element, index);
                break;
            case 4:
                display(arr, n);
                break;
            case 5:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice!\n");
        }
    } while (choice != 5);

    return 0;
}
Footer

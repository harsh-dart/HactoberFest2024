#include <stdio.h>
#include <stdlib.h> // Required for malloc and free

void reverseArrayUsingExtraArray(int arr[], int size) {
    // Dynamically allocate an array for the reversed elements
    int* reversedArr = (int*)malloc(size * sizeof(int));
    if (reversedArr == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }

    // Reverse the array
    for (int i = 0; i < size; i++) {
        reversedArr[i] = arr[size - i - 1];
    }

    // Print reversed array
    printf("Reversed Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", reversedArr[i]);
    }
    printf("\n"); // New line for better output formatting

    // Free dynamically allocated memory
    free(reversedArr);
}

int main() {
    int originalArr[] = { 1, 2, 3, 4, 5 };
    int size = sizeof(originalArr) / sizeof(originalArr[0]);

    reverseArrayUsingExtraArray(originalArr, size);

    return 0;
}

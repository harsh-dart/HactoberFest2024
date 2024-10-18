#include <stdio.h>
#include <stdlib.h>

void reverseArray(int arr[], int size) {
    // Dynamically allocate memory for the reversed array
    int *reversedArr = (int *)malloc(size * sizeof(int));
    if (reversedArr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
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
    printf("\n");

    // Free the allocated memory
    free(reversedArr);
}

int main() {
    int originalArr[] = { 1, 2, 3, 4, 5 };
    int size = sizeof(originalArr) / sizeof(originalArr[0]);

    reverseArray(originalArr, size);

    return 0;
}

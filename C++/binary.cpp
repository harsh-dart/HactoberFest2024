#include <iostream>
using namespace std;

// Function to perform binary search in a sorted 2D matrix
bool binarySearchInMatrix(int matrix[][4], int rows, int cols, int target) {
    int left = 0;
    int right = rows * cols - 1; // Treat the 2D matrix as a 1D array

    while (left <= right) {
        int mid = left + (right - left) / 2; // Find the middle index
        int midValue = matrix[mid / cols][mid % cols]; // Map the mid index to 2D matrix

        if (midValue == target) {
            cout << "Element found at (" << mid / cols << ", " << mid % cols << ")" << endl;
            return true;
        } else if (midValue < target) {
            left = mid + 1; // Search in the right half
        } else {
            right = mid - 1; // Search in the left half
        }
    }

    cout << "Element not found." << endl;
    return false;
}

int main() {
    // Example sorted matrix (3x4)
    int matrix[3][4] = {
        {1, 4, 7, 11},
        {2, 5, 8, 12},
        {3, 6, 9, 16}
    };

    int target = 5; // Element to search for

    binarySearchInMatrix(matrix, 3, 4, target); // Function call

    return 0;
}

#include <iostream>
#include <vector>
using namespace std;

// Function to search for a target in a 2D matrix
bool searchMatrix(const vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) {
        return false;
    }

    int m = matrix.size();    // number of rows
    int n = matrix[0].size(); // number of columns

    int left = 0;
    int right = m * n - 1; // Total elements are m * n

    // Binary search
    while (left <= right) {
        int mid = left + (right - left) / 2;  // Find the middle index
        int midValue = matrix[mid / n][mid % n]; // Convert mid index to 2D coordinates

        if (midValue == target) {
            return true; // Target found
        } else if (midValue < target) {
            left = mid + 1; // Move to the right half
        } else {
            right = mid - 1; // Move to the left half
        }
    }

    return false; // Target not found
}

int main() {
    vector<vector<int>> matrix = {
        {1, 3, 5, 7},
        {10, 11, 16, 20},
        {23, 30, 34, 60}
    };

    int target;
    cout << "Enter the target value: ";
    cin >> target;

    if (searchMatrix(matrix, target)) {
        cout << "Target " << target << " found in the matrix." << endl;
    } else {
        cout << "Target " << target << " not found in the matrix." << endl;
    }

    return 0;
}

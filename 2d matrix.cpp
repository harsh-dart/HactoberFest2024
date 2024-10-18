#include <iostream>
#include <vector>

bool searchMatrix(const std::vector<std::vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return false;

    int rows = matrix.size();
    int cols = matrix[0].size();
    int row = 0;
    int col = cols - 1;

    while (row < rows && col >= 0) {
        if (matrix[row][col] == target) {
            return true; // Found the target
        } else if (matrix[row][col] > target) {
            col--; // Move left
        } else {
            row++; // Move down
        }
    }

    return false; // Target not found
}

int main() {
    std::vector<std::vector<int>> matrix = {
        {1,  3,  5,  7},
        {10, 11, 16, 20},
        {23, 30, 34, 50},
        {60, 61, 66, 70}
    };

    int target;
    std::cout << "Enter the target value to search: ";
    std::cin >> target;

    bool found = searchMatrix(matrix, target);
    if (found) {
        std::cout << "Target " << target << " found in the matrix." << std::endl;
    } else {
        std::cout << "Target " << target << " not found in the matrix." << std::endl;
    }

    return 0;
}

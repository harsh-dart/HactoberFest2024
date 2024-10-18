#include <iostream>
#include <vector>
#include <algorithm>

// Function to get the digit at the specified position
int getDigit(int num, int pos) {
    return (num / pos) % 10;
}

// Function to perform Counting Sort based on a specific digit position
void countingSort(std::vector<int>& arr, int exp) {
    int n = arr.size();
    std::vector<int> output(n);
    std::vector<int> count(10, 0);

    // Store the count of occurrences in count[]
    for (int i = 0; i < n; i++) {
        count[getDigit(arr[i], exp)]++;
    }

    // Change count[i] so that count[i] now contains actual
    // position of this digit in output[]
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    // Build the output array
    for (int i = n - 1; i >= 0; i--) {
        output[count[getDigit(arr[i], exp)] - 1] = arr[i];
        count[getDigit(arr[i], exp)]--;
    }

    // Copy the output array to arr[], so that arr[] now contains
    // sorted numbers according to the current digit
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

// Main function that implements Radix Sort
void radixSort(std::vector<int>& arr) {
    // Find the maximum number to know the number of digits
    int maxNum = *std::max_element(arr.begin(), arr.end());

    // Do counting sort for every digit. exp is 10^i where i is the
    // current digit number
    for (int exp = 1; maxNum / exp > 0; exp *= 10) {
        countingSort(arr, exp);
    }
}

// Function to print the array
void printArray(const std::vector<int>& arr) {
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

// Example usage
int main() {
    std::vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    
    std::cout << "Original array: ";
    printArray(arr);
    
    radixSort(arr);
    
    std::cout << "Sorted array: ";
    printArray(arr);
    
    return 0;
}

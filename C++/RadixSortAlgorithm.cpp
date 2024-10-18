#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// A utility function to get the maximum value in an array
int getMax(const vector<int>& arr) {
    return *max_element(arr.begin(), arr.end());
}

// A function to do counting sort of arr[] according to the digit represented by exp
void countingSort(vector<int>& arr, int exp) {
    int n = arr.size();
    vector<int> output(n); // Output array
    int count[10] = {0};   // Count array to store the count of digits

    // Store the count of occurrences in count[]
    for (int i = 0; i < n; i++) {
        count[(arr[i] / exp) % 10]++;
    }

    // Change count[i] so that count[i] now contains the actual position of this digit in the output[]
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    // Build the output array
    for (int i = n - 1; i >= 0; i--) {
        int digit = (arr[i] / exp) % 10;
        output[count[digit] - 1] = arr[i];
        count[digit]--;
    }

    // Copy the output array to arr[], so that arr[] now contains the sorted numbers according to the current digit
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

// The main function to sort an array using Radix Sort
void radixSort(vector<int>& arr) {
    // Find the maximum number to determine the number of digits
    int maxVal = getMax(arr);

    // Do counting sort for every digit. Note that exp is 10^i where i is the current digit number
    for (int exp = 1; maxVal / exp > 0; exp *= 10) {
        countingSort(arr, exp);
    }
}

int main() {
    vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};

    cout << "Original array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    // Perform Radix Sort
    radixSort(arr);

    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}


#include <iostream>
#include <vector>   // For std::vector
#include <algorithm> // For sort()
using namespace std;

// Function to perform binary search
int binarySearch(const vector<int>& arr, int key) {
    int low = 0, high = arr.size() - 1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2; // Calculate mid

        // Check if the key is present at mid
        if (arr[mid] == key)
            return mid;

        // If key is greater, ignore the left half
        if (arr[mid] < key)
            low = mid + 1;

        // If key is smaller, ignore the right half
        else
            high = mid - 1;
    }

    // Key was not present in the array
    return -1;
}

int main() {
    int n, key;

    // Get the size of the array
    cout << "Enter the number of elements: ";
    cin >> n;

    // Use vector instead of a fixed-size array
    vector<int> arr(n);

    // Input the elements of the array
    cout << "Enter the elements of the array (sorted or unsorted):\n";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Sort the array in ascending order
    sort(arr.begin(), arr.end());

    // Display the sorted array
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Get the key to search
    cout << "Enter the element to search: ";
    cin >> key;

    // Perform binary search
    int result = binarySearch(arr, key);

    // Output the result
    if (result != -1)
        cout << "Element found at index: " << result << endl;
    else
        cout << "Element not found in the array" << endl;

    return 0;
}

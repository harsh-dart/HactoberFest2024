#include <iostream> // Corrected #include directive
using namespace std;

// Function to calculate x^n using efficient recursion (Exponentiation by Squaring)
double power(double x, int n) {
    // Base case: x^0 = 1
    if (n == 0)
        return 1;

    // If n is negative, convert to positive and invert x
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }

    // Recursive case: If n is even
    if (n % 2 == 0) {
        double halfPower = power(x, n / 2);
        return halfPower * halfPower;
    } 
    // If n is odd
    else {
        return x * power(x, n - 1);
    }
}

int main() {
    double x;
    int n;

    // Input base and exponent
    cout << "Enter the base (x): ";
    cin >> x;

    cout << "Enter the exponent (n): ";
    cin >> n;

    // Call the power function
    double result = power(x, n);

    // Display the result
    cout << x << "^" << n << " = " << result << endl;

    return 0;
}

#include <iostream>
using namespace std;

// Function to calculate power using Exponentiation by Squaring
double power(double x, int n) {
    // Base case: any number raised to the power of 0 is 1
    if (n == 0)
        return 1;

    // Recursive case: if n is negative, calculate for positive n and invert
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }

    // Recursive step: calculate power for half of n
    double halfPower = power(x, n / 2);

    // If n is even: x^n = (x^(n/2))^2
    if (n % 2 == 0)
        return halfPower * halfPower;

    // If n is odd: x^n = x * (x^(n/2))^2
    else
        return x * halfPower * halfPower;
}

int main() {
    double x;
    int n;

    cout << "Enter the base (x): ";
    cin >> x;
    cout << "Enter the exponent (n): ";
    cin >> n;

    double result = power(x, n);
    cout << x << "^" << n << " = " << result << endl;

    return 0;
}

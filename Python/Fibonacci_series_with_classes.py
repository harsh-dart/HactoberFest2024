class Fibonacci:
    def __init__(self):
        self.memo = {}  # Dictionary to store calculated Fibonacci numbers for optimization

    def calculate(self, n):
        # Base cases
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Check if Fibonacci number is already calculated
        if n in self.memo:
            return self.memo[n]
        
        # Calculate the Fibonacci number and store it in the dictionary (memoization)
        self.memo[n] = self.calculate(n-1) + self.calculate(n-2)
        return self.memo[n]

    def print_series(self, count):
        for i in range(count):
            print(self.calculate(i), end=" ")

# Example usage
fib = Fibonacci()
fib.print_series(10)  # Output: 0 1 1 2 3 5 8 13 21 34

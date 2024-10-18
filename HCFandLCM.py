import math

# Function to compute HCF
def compute_hcf(x, y):
    return math.gcd(x, y)

# Function to compute LCM
def compute_lcm(x, y):
    lcm = abs(x * y) // compute_hcf(x, y)
    return lcm

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate HCF and LCM
hcf = compute_hcf(num1, num2)
lcm = compute_lcm(num1, num2)

# Display the results
print(f"The HCF of {num1} and {num2} is: {hcf}")
print(f"The LCM of {num1} and {num2} is: {lcm}")

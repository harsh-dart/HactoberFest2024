# Function to calculate HCF (GCD) using Euclidean algorithm
def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to calculate LCM
def lcm(x, y):
    return (x * y) // hcf(x, y)

# Test the functions
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compute HCF and LCM
hcf_result = hcf(num1, num2)
lcm_result = lcm(num1, num2)

# Display the results
print(f"HCF of {num1} and {num2} is: {hcf_result}")
print(f"LCM of {num1} and {num2} is: {lcm_result}")

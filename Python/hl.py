def compute_hcf(x, y):
    # Euclidean algorithm to compute HCF
    while(y):
        x, y = y, x % y
    return x

def compute_lcm(x, y):
    # LCM is calculated using the formula: (x * y) // HCF(x, y)
    hcf = compute_hcf(x, y)
    return (x * y) // hcf

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate HCF and LCM
hcf = compute_hcf(num1, num2)
lcm = compute_lcm(num1, num2)

# Display the results
print(f"The HCF of {num1} and {num2} is: {hcf}")
print(f"The LCM of {num1} and {num2} is: {lcm}")

# Check if a number is prime
num = int(input("Enter a number: "))

# Negative numbers, 0 and 1 are not primes
if num <= 1:
    print(num, "is not a prime number")

else:
    # Iterate from 2 to num // 2
    for i in range(2, (num // 2) + 1):
        # If num is divisible by any number between 2 and num // 2, it's not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

num = int(input("Enter a number: "))  # Input the number to check

# Prime numbers are greater than 1
if num > 1:
    for i in range(2, (num // 2) + 1):
        # If num is divisible by any number between 2 and num // 2, it's not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        # This else belongs to the for-loop, not the if-statement
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")  # Handle numbers less than or equal to 1

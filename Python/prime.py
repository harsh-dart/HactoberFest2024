def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [11, 12, 13, 14, 15]  # Add your numbers here
results = {num: is_prime(num) for num in numbers}

for num, prime in results.items():
    print(f"{num} is {'a prime number' if prime else 'not a prime number'}")

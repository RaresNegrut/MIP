def sieve(n):
    # Create a boolean list of length n + 1 to store the prime numbers
    primes = [True] * (n + 1)
    
    # Set 0 and 1 to False (0 and 1 are not prime numbers)
    primes[0] = False
    primes[1] = False
    
    # Use a for loop to iterate over the range 2 to n
    for i in range(2, n + 1):
        # If the number is prime, set all of its multiples to False
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    
    # Use a list comprehension to return a list of the prime numbers
    return [i for i in range(2, n + 1) if primes[i]]

# Test the sieve function (ciurul lui eratostene)
print(sieve(20))  


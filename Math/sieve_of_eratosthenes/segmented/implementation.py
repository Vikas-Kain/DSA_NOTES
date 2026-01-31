import math

def simple_sieve(limit):
    """Standard Sieve to find primes up to sqrt(high)."""
    primes = []
    mark = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if mark[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                mark[i] = False
    return primes

def segmented_sieve(low, high):
    """
    Segmented Sieve of Eratosthenes.
    Finds all prime numbers in the range [low, high].
    """
    if low < 2:
        low = 2
    
    if low > high:
        return []

    # Step 1: Find all primes up to sqrt(high) using simple sieve
    limit = int(math.sqrt(high))
    primes = simple_sieve(limit)

    # Step 2: Create a boolean array for the range [low, high]
    # range_primes[i] represents the number (low + i)
    range_size = high - low + 1
    is_prime = [True] * range_size

    # Step 3: Use the primes found in step 1 to mark multiples in the range
    for p in primes:
        # Find the smallest multiple of p in the range [low, high]
        # that is greater than or equal to low
        start = (low // p) * p
        if start < low:
            start += p
        
        # If start is p itself, move to the next multiple
        if start == p:
            start += p
            
        # Mark multiples of p as False
        for j in range(start, high + 1, p):
            is_prime[j - low] = False

    # Step 4: Collect all primes in the range
    result = []
    for i in range(range_size):
        if is_prime[i]:
            result.append(low + i)
            
    return result

if __name__ == "__main__":
    # Example: Find primes between 10 and 50
    low = 10
    high = 50
    primes = segmented_sieve(low, high)
    print(f"Prime numbers between {low} and {high}:")
    print(primes)
    print("Total primes:", len(primes))
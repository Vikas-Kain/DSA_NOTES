def sieve_of_eratosthenes(N: int):
    """
    Returns a list of all prime numbers from 1 to N using
    the Sieve of Eratosthenes algorithm.
    """
    if N < 2:
        return []

    # Step 1: Initialize prime array
    primes = [True] * (N + 1)
    primes[0] = primes[1] = False

    # Step 2: Mark non-prime numbers
    for i in range(2, int(N ** 0.5) + 1):
        if primes[i]:
            # Start marking multiples from i*i
            for j in range(i * i, N + 1, i):
                primes[j] = False

    # Step 3: Collect prime numbers
    result = []
    for i in range(2, N + 1):
        if primes[i]:
            result.append(i)

    return result


# ---------------------------------------------------
# 🧪 Driver Code
# ---------------------------------------------------

if __name__ == "__main__":
    N = 50

    primes = sieve_of_eratosthenes(N)

    print(f"Prime numbers from 1 to {N}:")
    print(primes)

    print("\nTotal primes found:", len(primes))

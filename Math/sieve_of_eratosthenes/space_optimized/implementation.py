def sieve_optimized_space(N: int):
    """
    Optimized Sieve of Eratosthenes using only odd numbers.
    Space Complexity: O(N/2)
    """
    if N < 2:
        return []

    # Only odd numbers are represented
    size = (N // 2) + 1
    is_prime = [True] * size

    primes = [2]  # handle 2 separately

    # Iterate over odd numbers only
    for i in range(3, int(N ** 0.5) + 1, 2):
        if is_prime[i // 2]:
            # Mark odd multiples of i
            for j in range(i * i, N + 1, 2 * i):
                is_prime[j // 2] = False

    # Collect primes
    for i in range(3, N + 1, 2):
        if is_prime[i // 2]:
            primes.append(i)

    return primes

if __name__ == "__main__":
    N = 50
    primes = sieve_optimized_space(N)

    print(f"Prime numbers from 1 to {N}:")
    print(primes)
    print("Total primes:", len(primes))

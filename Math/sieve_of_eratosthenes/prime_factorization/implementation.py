def build_spf(N: int):
    """
    Builds Smallest Prime Factor (SPF) array for numbers up to N
    """
    spf = list(range(N + 1))  # spf[i] = i initially

    for i in range(2, int(N ** 0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i

    return spf

def prime_factorization(n: int, spf):
    """
    Returns prime factorization of n using SPF
    """
    factors = {}

    while n > 1:
        prime = spf[n]
        factors[prime] = factors.get(prime, 0) + 1
        n //= prime

    return factors

if __name__ == "__main__":
    MAX_N = 10**6

    # Precompute SPF
    spf = build_spf(MAX_N)

    numbers = [60, 84, 97, 1000000]

    for num in numbers:
        print(f"Prime factorization of {num}:")
        print(prime_factorization(num, spf))
        print()
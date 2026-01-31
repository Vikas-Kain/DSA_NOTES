# Prime Factorization Using Segmented Sieve

## 📌 Problem Statement

Given a number `N` (or multiple numbers in a range `[L, R]`), compute the **prime factorization** efficiently, even when `N` is large.

Traditional prime factorization becomes slow when:
- Numbers are large
- There are **multiple queries**
- Precomputing primes up to `N` is not feasible

---

## ❌ Limitations of Naive Factorization

Naive approach:
- Try dividing `N` by all numbers from `2` to `N`

**Time Complexity: O(N)**


**Even optimized trial division: O(√N)** 


❌ Too slow for large values or repeated queries

---

## 💡 Key Insight

If `N` is composite, then it has a prime divisor:
≤ √N


So:
- We only need primes up to `√R`
- Use **segmented sieve** to generate these primes
- Factor numbers efficiently using the precomputed primes

---

## 🧠 High-Level Strategy

1. Precompute all primes up to `√R` using Sieve / Segmented Sieve
2. For each number:
   - Try dividing by the precomputed primes
   - Reduce the number progressively
3. If remaining value > 1, it is a prime factor

---

## 🧩 Algorithm Overview

### Step 1: Generate Base Primes
Compute all prime numbers up to:
limit = ⌊ √R ⌋


### Step 2: Factorize Each Number
For each number `N`:
- For every prime `p ≤ √N`:
  - While `N % p == 0`, divide `N`
- If remaining `N > 1`, it is a prime factor

---

## 🧮 Why Segmented Sieve?

- Normal sieve up to `R` is memory-heavy
- Segmented sieve:
  - Uses only `O(√R)` memory
  - Supports large ranges
  - Ideal for repeated factorizations

---

## 🧩 Implementation

```python
import math

def generate_primes(limit: int):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return primes


def prime_factorization(N: int, primes):
    factors = {}

    for p in primes:
        if p * p > N:
            break
        while N % p == 0:
            factors[p] = factors.get(p, 0) + 1
            N //= p

    if N > 1:
        factors[N] = factors.get(N, 0) + 1

    return factors
```

---

## ⏱️ Time & Space Complexity
**Preprocessing: O(√R log log R)**

**Factorization per Number: O(√N / log N)**

**Space Complexity: O(√R)**

---
## 🚀 Why This Approach Is Important
Handles large numbers efficiently

Perfect for:

- Competitive programming
- Number theory problems
- Multiple factorization queries

Demonstrates:
- Sieve optimizations
- Mathematical reasoning
- Time–space trade-offs

## 🧠 Key Takeaways
- Factorization only needs primes up to √N
- Segmented sieve minimizes memory usage
- Reusing primes makes multiple queries fast
- Clean separation of preprocessing and queries

## 📚 References
Prime Factorization

- Sieve of Eratosthenes
- Number Theory Basics
- Segmented Sieve Technique
- Number Theory Basics
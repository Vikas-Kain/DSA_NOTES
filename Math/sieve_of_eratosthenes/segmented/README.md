# Segmented Sieve of Eratosthenes

## 📌 Problem Statement

Given a range `[L, R]`, find **all prime numbers in that range**, where `R` can be **very large** (up to `10^12` or more).

Using the normal Sieve of Eratosthenes up to `R` is **not memory feasible**.

---

## ❌ Why Normal Sieve Fails

Standard sieve requires:
O(R) space


If `R = 10^12`, storing an array of that size is impossible.

👉 We need a way to:
- Use **limited memory**
- Still mark composites efficiently

---

## 💡 Key Idea: Segmentation

Instead of sieving from `1` to `R`:

1. Precompute all primes up to `√R`
2. Divide the range `[L, R]` into manageable blocks (segments)
3. Use the small primes to mark composites **inside each segment only**

---

## 🧠 Mathematical Insight

If a number `n` is composite, it must have a prime factor:
≤ √n ≤ √R


So:
- All primes up to `√R` are sufficient to eliminate composites in `[L, R]`

---

## 🧩 Algorithm Overview

### Step 1: Precompute Base Primes
Use normal sieve to find all primes up to:
limit = ⌊ √R ⌋


### Step 2: Create Segment
Create a boolean array for numbers in `[L, R]`:
size = R - L + 1


### Step 3: Mark Multiples
For each base prime `p`:
- Find the first multiple of `p` in `[L, R]`
- Mark all multiples of `p` as non-prime

### Step 4: Collect Primes
Remaining unmarked numbers are primes

---

## 🧮 Finding First Multiple in Range

For a prime `p`, the first multiple in `[L, R]` is:

max(p * p, ceil(L / p) * p)


Why:
- Multiples smaller than `p²` were already handled earlier
- Ensures correctness and avoids redundant marking

---

## 🧩 Implementation

```python
def segmented_sieve(L: int, R: int):
    import math

    # Step 1: Sieve up to sqrt(R)
    limit = int(math.sqrt(R)) + 1
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    base_primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            base_primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Step 2: Create segment [L, R]
    segment = [True] * (R - L + 1)

    # Step 3: Mark multiples in the segment
    for p in base_primes:
        start = max(p * p, ((L + p - 1) // p) * p)
        for j in range(start, R + 1, p):
            segment[j - L] = False

    # Handle edge case where L = 1
    if L == 1:
        segment[0] = False

    # Step 4: Collect primes
    primes = []
    for i in range(L, R + 1):
        if segment[i - L]:
            primes.append(i)

    return primes
```

---

## ⏱️ Time & Space Complexity
**Time Complexity: O((R - L + 1) log log R)**

**Space Complexity: O(√R + (R - L + 1))**

Only small primes and one segment are stored at a time.

## 🚀 Why Segmented Sieve Is Important
Works for very large ranges

Essential for:
- Competitive programming
- Number theory problems
- Large prime range queries
- Shows advanced understanding of:
- Sieve optimizations
- Space-efficient algorithms

## 🧠 Key Takeaways
- Normal sieve is not scalable for large R
- Segmented sieve uses math + partitioning
- Precompute small primes once
- Efficient and memory-friendly

## 📚 References
- Sieve of Eratosthenes
- Number Theory Basics
- Segmented Sieve Technique
- Competitive Programming Handbook
# Finding Prime Numbers from 1 to N

## 📌 Problem Statement

Given an integer `N`, find **all prime numbers from 1 to N** efficiently.

A **prime number** is a number greater than `1` that has exactly two divisors:
- `1`
- itself

---

## 🧠 Important Theorems

### Theorem 1  
Every integer greater than `1` can be expressed as a **product of prime numbers**.

### Theorem 2  
If a number `n` is **composite**, then it has **at least one prime divisor ≤ √n**.

These theorems are the foundation of efficient prime-checking algorithms.

---

## ❌ Naive Approach

### Idea
For each number `i` from `2` to `N`, check if it is divisible by any number from `2` to `i - 1`.

### Pseudocode
```python
primes = [True] * (N + 1)
primes[0] = primes[1] = False

for i in range(2, N + 1):
    for j in range(2, i):
        if i % j == 0:
            primes[i] = False
            break
```

Time Complexity
O(N * √N)
❌ Too slow for large N

## ✅ Optimal Approach: Sieve of Eratosthenes
Key Idea:
If a number i is prime, then all its multiples are not prime.

Instead of checking divisibility repeatedly:

Start from 2

Mark multiples of each prime as non-prime

## 🔍 Optimization Insight
For a prime number i, we start marking multiples from:

i × i
Why?

All smaller multiples (2i, 3i, ...) are already marked by smaller primes

Based on Theorem 2

We only need to process numbers up to:

⌊ √N ⌋
## 🧪 Algorithm Steps
Create a boolean array primes[0..N], initialized to True

Mark 0 and 1 as False

For i from 2 to √N:

If primes[i] is True

Mark all multiples of i from i*i to N as False

Remaining True indices are prime numbers

## 🧩 Implementation
```python
def sieve_of_eratosthenes(N):
    primes = [True] * (N + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(N ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, N + 1, i):
                primes[j] = False

    return [i for i in range(2, N + 1) if primes[i]]
```

## ⏱️ Time & Space Complexity

**Time Complexity: O(N log log N)**

Explanation:

Each prime p marks about N / p multiples

Total work ≈ N (1/2 + 1/3 + 1/5 + ...)

This harmonic-like sum grows very slowly

**Space Complexity: O(N)**
## 🚀 Why This Algorithm Is Important
One of the most fundamental algorithms in DSA

Used in:

- Number theory problems

- Competitive programming

- Cryptography basics

## 📚 Key Takeaways
- Checking primes individually is inefficient

- Preprocessing using sieve is optimal

- i*i optimization is crucial

- Understanding math intuition makes code simpler

## 📖 References
Sieve of Eratosthenes

Number Theory Basics
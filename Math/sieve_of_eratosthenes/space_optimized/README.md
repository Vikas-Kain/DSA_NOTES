# Optimized Space Sieve of Eratosthenes

## 📌 Problem Statement

Given an integer `N`, find **all prime numbers from 1 to N** using **less memory** than the traditional Sieve of Eratosthenes.

The goal is to **optimize space** while keeping the same optimal time complexity.

---

## 🔍 Motivation for Optimization

In the standard Sieve of Eratosthenes:
- We store a boolean array of size `N + 1`
- We process **even and odd numbers**

However:
- Except for `2`, **all even numbers are not prime**
- Storing and processing them wastes memory and time

---

## 💡 Key Insight

- Handle the prime number `2` separately
- Store and process **only odd numbers**
- Reduce memory usage by approximately **50%**

### Index Mapping

Since only odd numbers are stored:

number = 2 × index + 1

index = number // 2


---

## 🧠 Algorithm Overview

1. If `N < 2`, return an empty list
2. Add `2` to the prime list
3. Create a boolean array for **odd numbers only**
4. Iterate over odd numbers up to `√N`
5. Mark odd multiples starting from `i × i`
6. Collect remaining primes

---

## 🧩 Implementation

```python
def sieve_optimized_space(N: int):
    if N < 2:
        return []

    size = (N // 2) + 1
    is_prime = [True] * size

    primes = [2]

    for i in range(3, int(N ** 0.5) + 1, 2):
        if is_prime[i // 2]:
            for j in range(i * i, N + 1, 2 * i):
                is_prime[j // 2] = False

    for i in range(3, N + 1, 2):
        if is_prime[i // 2]:
            primes.append(i)

    return primes
```

---
## ⏱️ Time & Space Complexity
**Time Complexity: O(N log log N)**

Same as the standard sieve, since the marking behavior remains unchanged.

**Space Complexity: O(N / 2)**

Only odd numbers are stored, reducing memory usage by half.

## 🚀 Why This Optimization Matters
Useful when N is large

- Common interview follow-up question

- Demonstrates:

 Mathematical reasoning

Index mapping tricks

Space–time trade-offs

## 🧠 Key Takeaways
- Even numbers (except 2) are never prime

- Storing only odd numbers halves memory usage

- Time complexity remains optimal

- A simple observation leads to a powerful optimization

## 📚 References
- Sieve of Eratosthenes

- Number Theory Basics

- Competitive Programming Prime Techniques
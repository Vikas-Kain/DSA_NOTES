# Dynamic Min / Max Query on an Online Stream (With Updates)

## 📌 Problem Statement

Design a data structure that processes an **online stream of integers** and supports:

- Updating a value at any previous index
- Querying the **minimum** and **maximum** values at any point in time

This is a generalized version of **LeetCode 2034 – Stock Price Fluctuation**.

---

## 🧩 Example

Initial stream:
[2, 4, 1, 8, 0, 4]

Operations:
Query = [update, update, update, find, update, find, update, find]
Values = [(0,2), (2,1), (1,2), -, (1,4), -, (1,0), -]

arduino
Copy code

Stream evolution:
[2, 2, 1] → [2, 4, 1] → [2, 0, 1]

makefile
Copy code

Results:
Max = 2 → 4 → 2
Min = 1 → 1 → 0

yaml
Copy code

---

## ❌ Why a Simple Approach Fails

### 1. Tracking only `min` and `max`
- Works **only** when values are appended
- Breaks when older values are updated

### 2. Heap + Direct Update
- Modifying a value inside a heap costs `O(n)`
- Re-heapifying also costs `O(n)`
- Inefficient for frequent updates

👉 **Root problem:** trying to update heap values immediately

---

## 💡 Key Insight: Lazy (Eventual) Updates

Instead of modifying old values inside the heap:

- Keep all values in heaps
- Track which values are **currently valid**
- Discard invalid values **only when querying**

This pattern is called **lazy deletion**.

---

## 🧠 Data Structures Used

| Data Structure | Purpose |
|---------------|--------|
| `min_heap` | Retrieve minimum value |
| `max_heap` | Retrieve maximum value |
| `val_freq` (HashMap) | Frequency of valid values |
| `index_to_val` (HashMap) | Latest value at each index |

---

## 🔄 Update Operation

When updating index `i` from `old_val` → `new_val`:

```python
val_freq[old_val] -= 1
val_freq[new_val] += 1

heapq.heappush(min_heap, new_val)
heapq.heappush(max_heap, -new_val)

index_to_val[i] = new_val
```

- Old values remain in heaps

- Their frequency is reduced

- They become logically invalid

## 🔍 Find Min / Max Operation
Before returning heap top, clean invalid values:

python
Copy code
while val_freq[min_heap[0]] == 0:
    heapq.heappop(min_heap)

while val_freq[-max_heap[0]] == 0:
    heapq.heappop(max_heap)
This guarantees correctness without costly heap updates.

## ⏱️ Time & Space Complexity
Operation	Complexity
Update	O(log n)
Find Min / Max	Amortized O(log n)
Space	O(n)

## 🚀 Why This Pattern Is Important
Very common interview problem pattern

Used in:

- Stock price systems

- Streaming analytics

- Real-time dashboards

## 📚 References
LeetCode 2034 – Stock Price Fluctuation

Heap + HashMap Lazy Deletion Pattern
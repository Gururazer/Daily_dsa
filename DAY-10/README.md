# Day 10 - Minimum Operations to Make Array Elements Zero

**Problem Link**: [LeetCode 3495 - Minimum Operations to Make Array Elements Zero](https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/)  
**Difficulty**: Hard

## 💡 Approach

This problem is solved using a prefix sum technique for efficient range queries.

- First, we determine the number of operations each individual integer needs to become zero. An operation is floor(x/4), which is a right bit shift by 2. This means a number n needs k operations if 4^k−1 ≤ n < 4^k.
- A helper function `get(num)` calculates the total number of operations for all integers from 1 up to `num` by summing the operations for each group of numbers that require the same number of operations.
- For each query [l, r], the total operations for the range are efficiently calculated using the prefix sum: `get(r) - get(l-1)`.
- Finally, since each operation can reduce two numbers at once, the total number of operations for the query is this sum divided by two, rounded up: `(total_operations + 1) // 2`. We sum this value for all queries to get the final answer.

## ⏱️ Complexity

- **Time**: O(N + Q * log(max_val)) - The `get` function has a complexity related to the number of powers of 4 up to `num`, which is log(num). The loop runs for each query.
- **Space**: O(1) - The solution uses a constant amount of extra space.

## 📸 Screenshot
![Screenshot Placeholder](screenshot.png)
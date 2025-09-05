# Day 9 - Minimum Operations to Make the Integer Zero

**Problem Link**: [LeetCode 2749 - Minimum Operations to Make the Integer Zero](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/)  
**Difficulty**: Medium

## 💡 Approach

We solve this by iteratively subtracting `num2` and checking if the resulting number can be made zero with a specific number of operations.

- Start with `new_num = num1` and operation count `cnt = 1`.
- In each iteration:
  - Subtract `num2` from `new_num`.
  - Check if `new_num < cnt`: if true, return -1 (impossible to make zero).
  - Check if `cnt >= new_num.bit_count()` (number of 1s in binary representation of `new_num`): if true, return `cnt` as the minimum operations needed.
  - Increment `cnt` and continue.
- If the loop continues without meeting the condition, return -1.

## ⏱️ Complexity

- **Time**: O(log num1) – The loop runs proportional to the number of subtractions needed, which is bounded by the size of `num1`.
- **Space**: O(1) – Only a constant amount of extra space is used.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
# Day 61 - Number of Laser Beams in a Bank

**Problem Link**: [LeetCode 2125 - Number of Laser Beams in a Bank](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/)  
**Difficulty**: Medium

## 💡 Approach

We solve this by iterating through the rows of the bank to count security devices and calculate laser beams between consecutive non-empty rows.

- If the number of rows `n` is less than 2, return 0 (no beams possible).
- Initialize pointers `curr` (starting at 0) and `next` (starting at `curr + 1`).
- Initialize `ans` to store the total number of beams.
- While `next` is within bounds:
  - Count security devices (`1`s) in the `curr` row as `n1` using `count('1')`.
  - Count security devices in the `next` row as `n2`.
  - If `n2` is 0 and `next` is not the last row, increment `next` until a row with devices is found or the end is reached.
  - Add the product `n1 * n2` to `ans` (number of beams between these rows).
  - Update `curr` to `next` and increment `next`.
- Return `ans`, the total number of laser beams.

## ⏱️ Complexity

- **Time**: O(m * n) - Where `m` is the number of rows and `n` is the length of each row (for counting '1's in each row).
- **Space**: O(1) - Only constant extra space is used.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
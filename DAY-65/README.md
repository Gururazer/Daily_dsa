# Day 65 - The Two Sneaky Numbers of Digitville

**Problem Link**: [LeetCode 3289 - The Two Sneaky Numbers of Digitville](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/)  
**Difficulty**: Easy

## Approach

We solve this by using a set to track seen numbers and identifying duplicates as they appear.

- Initialize:
  - `hmp`: a set to store numbers we've seen.
  - `res`: a list to store the two sneaky (duplicate) numbers.
  - `i`: index to traverse the array.
- Traverse `nums` until `res` contains 2 elements:
  - If `nums[i]` is already in `hmp`, it’s a duplicate → append to `res`.
  - Otherwise, add `nums[i]` to `hmp`.
  - Increment `i`.
- Return `res` containing the two numbers that appear more than once.

> The problem guarantees exactly two numbers appear twice.

## Complexity

- **Time**: **O(n)** — single pass through the array
- **Space**: **O(n)** — for the set and result list

## Screenshot
![Solution Screenshot](screenshot.png)
# Day 8 - Find Closest Person

**Problem Link**: [LeetCode 3516 - Find Closest Person](https://leetcode.com/problems/find-closest-person/)  
**Difficulty**: Easy

## 💡 Approach

We solve this by comparing absolute distances between positions.

- Given three integers `x`, `y`, `z` (positions of person 1, person 2, and person 3), compute distances: `|z - x|` and `|z - y|`.
- If `|z - x| < |z - y|`, return 1 (person 1 is closer).
- If `|z - x| > |z - y|`, return 2 (person 2 is closer).
- If distances are equal, return 0.

## ⏱️ Complexity

- **Time**: O(1) – Constant time for distance calculations and comparison.
- **Space**: O(1) – No extra space required.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
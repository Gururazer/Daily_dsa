# Day 42 - Successful Pairs of Spells and Potions

**Problem Link**: [LeetCode 2300 - Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)  
**Difficulty**: Medium

## 💡 Approach

We solve this using binary search to efficiently count successful spell-potion pairs.

- Sort the `potions` array in ascending order.
- For each `spell` in `spells`:
  - Calculate the required potion strength `req_str = (success + spell - 1) // spell` to achieve at least `success` when multiplied.
  - Use binary search (`bisect_left`) to find the index `k` of the smallest potion value ≥ `req_str`.
  - The number of successful pairs for the spell is `m - k`, where `m` is the length of `potions`.
  - Append this count to the result list `pairs`.
- Return the `pairs` list containing the count of successful pairs for each spell.

## ⏱️ Complexity

- **Time**: O(n log m + m log m) - Sorting `potions` takes O(m log m), and binary search for each of the n spells takes O(log m), where n is the length of `spells` and m is the length of `potions`.
- **Space**: O(n) - For the output array `pairs` (excluding input storage).

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
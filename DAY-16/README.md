# Day 16 - Vowels Game in a String

**Problem Link**: [LeetCode 3227 - Vowels Game in a String](https://leetcode.com/problems/vowels-game-in-a-string/)  
**Difficulty**: Medium

## 💡 Approach

We solve this by checking for the presence of any vowel in the string to determine if Alice wins the game.

- Define a list of vowels (`a, e, i, o, u`).
- Iterate through the vowels and check if any vowel exists in the string `s`.
- If at least one vowel is found, return `True` (Alice wins).
- If no vowels are found, return `False` (Alice loses).

## ⏱️ Complexity

- **Time**: O(n) - Iterating through the string to check for each vowel is O(n) in the worst case, where n is the string length.
- **Space**: O(1) - Constant space for the vowel list.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
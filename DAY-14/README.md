# Day 14 - Minimum Number of People to Teach

**Problem Link**: [LeetCode 1733 - Minimum Number of People to Teach](https://leetcode.com/problems/minimum-number-of-people-to-teach/)  
**Difficulty**: Medium

## 💡 Approach

We solve this using a greedy approach with set operations to minimize the number of people taught a common language.

- Convert each user's language list to a set for efficient intersection checks.
- Identify pairs of friends who cannot communicate (no common language) by checking if their language sets have no intersection.
- If no such pairs exist, return 0 (no teaching needed).
- For each language from 1 to `n`:
  - Collect users from uncommunicative pairs who don't know the current language.
  - Use a set to track unique users who need to be taught.
  - Compute the number of users to teach for the current language.
- Return the minimum number of users to teach across all languages.

## ⏱️ Complexity

- **Time**: O(n * m + f * n), where `n` is the number of languages, `m` is the number of users, and `f` is the number of friendships. Language set conversion is O(m * l) (l = avg languages per user), friendship checks are O(f * l), and iterating languages over pairs is O(n * f).
- **Space**: O(m + f) - Space for language sets and uncommunicative pairs.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
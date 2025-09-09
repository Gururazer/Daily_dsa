# Day 13 - Number of People Aware of a Secret

**Problem Link**: [LeetCode 2327 - Number of People Aware of a Secret](https://leetcode.com/problems/number-of-people-aware-of-a-secret/)  
**Difficulty**: Medium

## 💡 Approach

We solve this using dynamic programming to track the number of people who learn the secret each day and manage the sharing window.

- Initialize `new_people[1] = 1` (one person learns the secret on day 1).
- Use `sharing` to track the number of people who can share the secret on the current day (those who learned it between `day-delay` and `day-forget` days ago).
- Use `total_aware` to track the total number of people who currently know the secret.
- For each day from 2 to n:
  - If `day > delay`, add the people who learned the secret `delay` days ago to the sharing pool.
  - If `day > forget`, remove the people who learned the secret `forget` days ago from the sharing pool and from total_aware.
  - The number of newly aware people today is equal to the current sharing pool.
  - Update `new_people[day]` and add to `total_aware`.
- Return `total_aware` modulo 10^9 + 7.

## ⏱️ Complexity

- **Time**: O(n) - Single pass through n days with constant time operations.
- **Space**: O(n) - Array to store new people learning each day.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
# Day 88 - Greatest Sum Divisible by Three

**Problem Link**: [LeetCode 1262 - Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/)  
**Difficulty**: Medium

## Approach

We solve this using a **greedy strategy** after sorting:  
**Maximize the sum** while making it divisible by 3 by **removing the smallest possible amount**.

### Key Insight:
> Let `total = sum(nums)`  
> If `total % 3 == 0` → return `total`  
> Else, we need to remove some numbers so that the remaining sum is divisible by 3.

We only care about numbers with:
- `x % 3 == 1` → removing one reduces sum by 1 mod 3
- `x % 3 == 2` → removing one reduces sum by 2 mod 3

### Cases:
Let `total % 3 = r`

- If `r == 1`:
  - Option 1: Remove **one** number with `x % 3 == 1`
  - Option 2: Remove **two** numbers with `x % 3 == 2`
  - Choose the one that removes **least** value
- If `r == 2`:
  - Option 1: Remove **one** number with `x % 3 == 2`
  - Option 2: Remove **two** numbers with `x % 3 == 1`
  - Choose minimum removal

### Steps:
1. Sort `nums` → helps pick smallest candidates
2. Separate numbers into `mod1` (≡1 mod 3) and `mod2` (≡2 mod 3)
3. Compute total sum
4. If `total % 3 == 0` → return it
5. Else compute the **minimum removable amount** using the two options above
6. Return `total - min_removal`

### Example: `nums = [3,6,5,1,8]`
- Sum = 23 → 23 % 3 = 2
- Need to remove amount ≡ 2 mod 3
- `mod2 = [8,5]` → smallest two: 5+8=13
- `mod1 = [1]` → can't remove two
- So remove 5 → new sum = 18 → divisible by 3

## Complexity

- **Time**: **O(n log n)** — due to sorting
- **Space**: **O(n)**

## Screenshot
![Solution Screenshot](screenshot.png)
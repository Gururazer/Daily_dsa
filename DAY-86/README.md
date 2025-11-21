# Day 86 - Unique Length-3 Palindromic Subsequences

**Problem Link**: [LeetCode 1930 - Unique Length-3 Palindromic Subsequences](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/)  
**Difficulty**: Medium

## Approach

We solve this using a **three-pointer-like idea** with **sets and frequency tracking** to count unique palindromes of form `aba`.

### Key Insight:
> A palindrome `aba` exists if:
> - There is a **left** occurrence of `a`
> - A **middle** occurrence of `b`
> - A **right** occurrence of `a` (after middle)

We can simulate this by:
- Maintaining `left`: set of characters seen so far
- Maintaining `right`: frequency of remaining characters
- For each middle character `m`, check if any `ele` in `left` has at least one occurrence left in `right`

### Steps:
1. Initialize:
   - `left = set()` → characters seen before current
   - `right = Counter(s)` → remaining characters
   - `ans = set()` → store unique `(a,b)` pairs for `aba`
2. For each character `m` in `s`:
   - Decrease its count in `right`
   - For every character `ele` in `left`:
     - If `right[ele] >= 1` → there is a future `ele` → `(ele, m)` forms a valid `aba`
     - Add `(ele, m)` to `ans`
   - Add `m` to `left`

### Example: `s = "aabca"`
- `m='a'`: left={}, skip
- `m='a'`: left={'a'}, right['a']=1 → add ('a','a') → "aaa"
- `m='b'`: left={'a'}, right['a']=1 → add ('a','b') → "aba"
- `m='c'`: left={'a','b'}, right['a']=1 → add ('a','c') → "aca"
- `m='a'`: left={'a','b','c'}, right['a']=0 → no new

→ Unique: `aaa`, `aba`, `aca` → **3**

## Complexity

- **Time**: **O(n × 26²)** ≈ **O(n)** in practice (since alphabet size is 26)
- **Space**: **O(1)** — bounded by 26×26 = 676 possible pairs

## Screenshot
![Solution Screenshot](screenshot.png)
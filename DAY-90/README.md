# Day 90 - Smallest Integer Divisible by K

**Problem Link**: [LeetCode 1015 - Smallest Integer Divisible by K](https://leetcode.com/problems/smallest-integer-divisible-by-k/)  
**Difficulty**: Medium

## Approach

We solve this by **simulating the construction** of the repunit number `111...1` and checking its remainder when divided by `K`.

### Key Insight:
> We want the smallest `N` such that `111...1` (N ones) is divisible by `K`.  
> This is equivalent to finding the smallest `N` where:  
> `(10^N - 1)/9 ≡ 0 mod K` → i.e., `10^N ≡ 1 mod (9K)` — but we can do better!

Instead, we compute the running value of `111...1 mod K`:
- Start with `curr = 1`
- At each step: `curr = (curr * 10 + 1) % K`
- If `curr == 0` → we found it!

But we must detect **cycles**: if the same remainder repeats, it's impossible.

### Steps:
1. Initialize:
   - `curr = 1` → value of "1" mod K
   - `ans = 1` → current length
   - `prev` = set to track seen remainders
2. While `curr % K != 0`:
   - If `curr` already seen → cycle detected → **return -1**
   - Add `curr` to `prev`
   - Update: `curr = (curr * 10 + 1) % K`
   - Increment `ans`
3. Return `ans`

### Example: `K = 3`
- `curr = 1` → `1 % 3 = 1`
- `curr = 11` → `11 % 3 = 2`
- `curr = 111` → `111 % 3 = 0` → **return 3**

### Example: `K = 7`
- After 6 steps: `curr = 111111 % 7 = 0` → **return 6**

## Complexity

- **Time**: **O(K)** — at most K distinct remainders
- **Space**: **O(K)** — for the set

## Screenshot
![Solution Screenshot](screenshot.png)
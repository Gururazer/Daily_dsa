# Day 28 - Fraction to Recurring Decimal

**Problem Link**: [LeetCode 166 - Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/)  
**Difficulty**: Medium

## 💡 Approach

We solve this by long division simulation, using a dictionary to detect repeating remainders for the fractional part.

- Handle special case: if `numerator == 0`, return `"0"`.
- Determine sign: if `numerator` and `denominator` have different signs, prepend `"-"` to result.
- Take absolute values for both `numerator` and `denominator`.
- Compute integer part (`whole = numerator // denominator`) and append to result.
- Compute remainder (`remainder = numerator % denominator`).
- If remainder is 0, return the joined result (no fractional part).
- Append `"."` for fractional part.
- Use `remainder_map` to track seen remainders and their positions in result.
- Simulate division for fractional digits:
  - Multiply remainder by 10.
  - Append digit (`remainder // denominator`) to result.
  - Update remainder (`remainder % denominator`).
  - If remainder seen before, insert `"("` at the position and append `")"` to mark repeating part.
  - Otherwise, record current remainder's position.
- Return the joined result string.

## ⏱️ Complexity

- **Time**: O(D) - Where D is the denominator's magnitude; the fractional part length is bounded by D before remainder repeats.
- **Space**: O(D) - For the `remainder_map` and result list in the worst case.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
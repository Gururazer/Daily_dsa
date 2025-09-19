# Day 23 - Design Spreadsheet

**Problem Link**: [LeetCode 3484 - Design Spreadsheet](https://leetcode.com/problems/design-spreadsheet/)  
**Difficulty**: Medium

## 💡 Approach

We solve this by implementing a spreadsheet with a grid to store values and helper functions to parse and evaluate cell references and formulas.

- **Initialization**: Create a grid of size `rows x 26` (for columns A-Z) initialized with zeros.
- **_parse_cell**: Convert a cell reference (e.g., "A1") to grid indices by extracting column (A-Z to 0-25) and row (1-based to 0-based).
- **setCell**: Set the value at the parsed cell's row and column in the grid.
- **resetCell**: Set the value at the parsed cell's row and column to 0.
- **getValue**: Parse a formula (e.g., "=A1+5" or "=A1+B2"), split by '+' to get two parts, evaluate each part using `_evaluate_part`, and return their sum.
- **_evaluate_part**: If the part is a digit, convert to integer; otherwise, parse as a cell reference and return the grid value at that position.

## ⏱️ Complexity

- **Time**:
  - `__init__`: O(rows) - Initialize grid of size rows x 26.
  - `setCell`: O(1) - Single grid update.
  - `resetCell`: O(1) - Single grid update.
  - `getValue`: O(1) - Parse formula and access grid (fixed two-part formula).
  - `_evaluate_part`: O(1) - Parse cell or convert digit.
- **Space**: O(rows) - Grid storage (rows x 26).

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
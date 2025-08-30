# Day 3 - Valid Sudoku  

**Problem Link:** [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)  
**Difficulty:** Medium  

---

## 💡 Approach
- Use sets to track seen digits in each row, column, and 3x3 sub-box.  
- If a duplicate is found, return False.  
- Otherwise, return True after scanning the board.  

---

## ⏱️ Complexity
- Time: **O(9^2) = O(81) → O(1)** (constant since board is fixed size)  
- Space: **O(1)** (though uses sets for bookkeeping)  

---

## 📸 Screenshot
![Valid Sudoku](screenshot.jpg)

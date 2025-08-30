# Day 02 - Merge Sorted Array  

**Problem Link:** [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)  
**Difficulty:** Easy  

---

## 💡 Approach
- Start merging from the back (m+n-1 index).  
- Compare `nums1[m-1]` and `nums2[n-1]`, put the larger at the end.  
- Continue until all elements are placed.  

---

## ⏱️ Complexity
- Time: **O(m+n)**
- Space: **O(1)**  

---

## 📸 Screenshot
![Merge Sorted Array](screenshot.png)

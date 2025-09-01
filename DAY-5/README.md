Day 5 - Maximum Average Pass Ratio
Problem Link: LeetCode 1792 - Maximum Average Pass Ratio
Difficulty: Medium

💡 Approach
Solved using a greedy algorithm with a max-heap (priority queue).

The core idea is to always add an extra student to the class that provides the largest marginal gain in the pass ratio.

A max-heap is used to efficiently select the class with the highest gain at each step.

⏱️ Complexity
Time: ‘O(k⋅logn)‘, where k is the number of extra students and n is the number of classes.

Space: ‘O(n)‘ for the heap.

📸 Screenshot
# Day 66 - Delete Nodes From Linked List Present in Array

**Problem Link**: [LeetCode 3217 - Delete Nodes From Linked List Present in Array](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/)  
**Difficulty**: Medium

## Approach

We solve this by using a hash set to store values to delete and traversing the linked list to remove matching nodes.

- Convert `nums` into a `set` (`hmp`) for **O(1)** lookup.
- **Skip leading nodes** that need to be deleted:
  - While `head.val` is in `hmp`, move `head` forward.
- Traverse the list using two pointers:
  - `prev`: points to the last valid node.
  - `curr`: current node being checked.
- For each node:
  - If `curr.val` is in `hmp`, **bypass** it: `prev.next = curr.next`.
  - Otherwise, move `prev` forward.
  - Always move `curr` forward.
- After the loop, check if the last node (`curr`) needs deletion → set `prev.next = None` if yes.
- Return the updated `head`.

## Complexity

- **Time**: **O(n + m)** — `n` = length of linked list, `m` = length of `nums`
- **Space**: **O(m)** — for the hash set

## Screenshot
![Solution Screenshot](screenshot.png)
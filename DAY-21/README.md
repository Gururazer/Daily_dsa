# Day 21 - Design a Food Rating System

**Problem Link**: [LeetCode 2353 - Design a Food Rating System](https://leetcode.com/problems/design-a-food-rating-system/)  
**Difficulty**: Medium

## 💡 Approach

We solve this using hash maps and max-heaps (priority queues) per cuisine to efficiently track and update food ratings.

- **Initialization**: 
  - Use `food_to_rating` dict to map foods to their ratings.
  - Use `food_to_cuisine` dict to map foods to their cuisines.
  - Use `cuisine_to_pq` defaultdict of lists to maintain a max-heap for each cuisine (using negative ratings for Python's min-heap).
  - Push `(-rating, food)` tuples into the respective cuisine heap.
- **changeRating**: Update the rating in `food_to_rating` and push the new `(-newRating, food)` into the cuisine's heap (lazy update).
- **highestRated**: 
  - Access the cuisine's heap.
  - While the top heap element's rating (negated) doesn't match the current `food_to_rating[food]`, pop it (remove stale entries).
  - Return the food from the valid top entry.
- This lazy deletion ensures heaps don't grow unbounded while keeping operations efficient.

## ⏱️ Complexity

- **Time**: 
  - `__init__`: O(n log n) - n pushes into heaps.
  - `changeRating`: O(log m) - Single push, where m is foods in a cuisine.
  - `highestRated`: Amortized O(log m) - Pops are bounded by total updates.
- **Space**: O(n) - For dicts and heaps storing all foods.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
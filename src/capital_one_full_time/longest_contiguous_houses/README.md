# Longest Contiguous Houses Problem

### Leetcode Adjacent Problem Link: [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/)

### Problem: Building Houses on Lots

You are given an array of queries where each element represents the position of a house being built on a street. After each house is built, determine the length of the longest contiguous segment of houses. Each query is guaranteed to have a unique position for a house.

### Input:

- **queries**: An array of integers representing house positions (all positions are unique)

### Output:

An array of integers where each element represents the length of the longest contiguous segment after each house is built

### Example:

Input:
```python
queries = [2, 1, 3, 5, 4]
```

Output:
```python
[1, 2, 3, 3, 5]
```

Explanation:
- Build at position 2: Houses at [2], longest = 1
- Build at position 1: Houses at [1,2], longest = 2
- Build at position 3: Houses at [1,2,3], longest = 3
- Build at position 5: Houses at [1,2,3] and [5], longest = 3
- Build at position 4: Houses at [1,2,3,4,5], longest = 5

# Digital Root Frequency Problem

### Leetcode Adjacent Problem Link: 
- [https://leetcode.com/problems/add-digits/](https://leetcode.com/problems/add-digits/)
- [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

### Problem: Sum Digits Until Single & Find Frequency

Given an array of positive integers, for each number: Sum its digits repeatedly until you get a single digit (digital root). Count the frequency of each resulting single digit. Return the digit with the highest frequency. If multiple digits have the same frequency, return the highest digit.

### Input:

- **numbers**: An array of positive integers

### Output:

The single digit with highest frequency (or highest value if tied)

### Example:

Input:
```python
numbers = [38, 29, 47, 156, 99]
```

Output:
```python
2
```

Explanation:
- 38 → 3+8=11 → 1+1=2
- 29 → 2+9=11 → 1+1=2  
- 47 → 4+7=11 → 1+1=2
- 156 → 1+5+6=12 → 1+2=3
- 99 → 9+9=18 → 1+8=9

Frequency: 2 appears 3 times, 3 appears 1 time, 9 appears 1 time

Result: 2 (highest frequency)

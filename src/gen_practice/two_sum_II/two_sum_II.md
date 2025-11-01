# Two Sum II - Input Array Is Sorted
- Attempt: [two_sum_II.py](./two_sum_II.py)
- Date: 10/05/2025
- Problem Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Phase 1: Set up

### Understanding the Question:

We are given two pieces of data:
- numbers = array[int] (1-indexed, sorted in non-decreasing order)
- target = int

Key differences from Two Sum I:
- Array is **already sorted** in non-decreasing order
- Returns **1-indexed** positions (not 0-indexed)
- Must use **constant extra space** O(1)
- Exactly one solution exists

We need to find two numbers that add up to target and return their 1-indexed positions [index1, index2] where index1 < index2.

### Constraints:

- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- Exactly one solution exists (guaranteed)

### Edge Cases:

- Two element array (minimum size)
- Negative numbers
- Target is negative or zero
- Duplicate numbers in array
- Solution uses first and last elements
- Solution uses adjacent elements

### Writing Test Cases:

**Test Case 1:**
```python
numbers = [2, 7, 11, 15], target = 9
# Expected: [1, 2]
# 2 + 7 = 9, indices 1 and 2 (1-indexed)
```

**Test Case 2:**
```python
numbers = [2, 3, 4], target = 6
# Expected: [1, 3]
# 2 + 4 = 6, indices 1 and 3 (1-indexed)
```

**Test Case 3:**
```python
numbers = [-1, 0], target = -1
# Expected: [1, 2]
# -1 + 0 = -1, indices 1 and 2 (1-indexed)
```

**Test Case 4:**
```python
numbers = [5, 25, 75], target = 100
# Expected: [2, 3]
# 25 + 75 = 100
```

## Phase 2: Approach

### Possible Approaches:

**Brute Force Approach:** 
Use nested loops to check every combination of two numbers until we find the pair that sums to target. Since we need constant space, this is technically valid but inefficient.

**Optimized Approach (Two Pointers):** 
Since the array is sorted, we can use two pointers - one at the start and one at the end. 
- If current sum < target, move left pointer right (increase sum)
- If current sum > target, move right pointer left (decrease sum)  
- If current sum == target, return the indices

**Hash Map Approach (Not optimal here):**
While this works, it uses O(n) space which violates the constant space requirement. The two-pointer approach is superior for sorted arrays.

### Estimated Time Complexity:

**Brute Force Approach:**
- Time complexity: O(n^2) - nested loops
- Space complexity: O(1) - no extra space

**Optimized Approach (Two Pointers):**
- Time complexity: O(n) - single pass with two pointers
- Space complexity: O(1) - only two pointer variables

**Hash Map Approach:**
- Time complexity: O(n) - single pass
- Space complexity: O(n) - hash map storage (violates constraint)

### Best approach:

The **two-pointer approach** is optimal for this problem because:
1. Array is already sorted (key advantage)
2. Achieves O(n) time complexity
3. Uses O(1) space (meets constant space requirement)
4. Simple and elegant solution

The sorted array is the critical factor that makes two pointers superior to hash map here.

### Skeleton Structure:

1. Initialize two pointers: left = 0 (start), right = len(numbers) - 1 (end)

2. While left < right:
   - Calculate current_sum = numbers[left] + numbers[right]
   
3. If current_sum == target:
   - Return [left + 1, right + 1] (convert to 1-indexed)
   
4. If current_sum < target:
   - Move left pointer right (left += 1) to increase sum
   
5. If current_sum > target:
   - Move right pointer left (right -= 1) to decrease sum

6. If no solution found (shouldn't happen per constraints):
   - Raise ValueError

## Phase 3: Code

### Coding the solution:

[two_sum_II.py](./two_sum_II.py)

```python
def two_sum_II(nums: List[int], target: int) -> List[int]:
    start_pointer, end_pointer = 0, len(nums) - 1

    while start_pointer < end_pointer:
        two_sum = nums[start_pointer] + nums[end_pointer]
        if two_sum == target:
            return [start_pointer + 1, end_pointer + 1]
        if two_sum > target:
            end_pointer -= 1
        else:
            start_pointer += 1
    
    raise ValueError("Not a valid input, missing required unique solution")
```

### Debugging Code:

Initial implementation was clean. Key considerations:
- Remember to return 1-indexed positions (add 1 to both pointers)
- Ensure loop condition is `start_pointer < end_pointer` (not <=)
- Error handling for impossible cases (though guaranteed by problem)

### Reviewing Code:

The implementation is optimal and clean:
- ✅ Uses only constant space O(1)
- ✅ Single pass through array O(n) time
- ✅ Takes advantage of sorted array property
- ✅ Returns 1-indexed positions as required
- ✅ Simple logic with clear pointer movements

No unnecessary edge case checks needed since:
- Problem guarantees exactly one solution exists
- Minimum array length is 2 (guaranteed by constraints)

### Potential better approach:

This is the optimal solution for this problem. Cannot improve on:
- O(n) time complexity
- O(1) space complexity

The two-pointer approach is perfect when:
- Array is sorted
- Constant space is required
- Looking for pair sum

For unsorted arrays, hash map (O(n) space) would be necessary, but here we leverage the sorted property for optimal performance.

## Phase 4: Testing

### Test Results:

All 27 unit tests passing ✅
- Basic cases and LeetCode examples
- Edge cases (negatives, duplicates, zeros)
- Performance tests with large arrays
- Error handling

Test coverage includes:
- Two element arrays
- Negative numbers and mixed signs
- Duplicate values
- Various pointer movement patterns
- Large arrays (up to 10,000 elements)

## Phase 5: Time Complexity

### Big-O:

- **Time complexity:** O(n) - Single pass with two pointers converging
- **Space complexity:** O(1) - Only two integer variables for pointers

### Comparison with Two Sum I:

| Aspect | Two Sum I | Two Sum II |
|--------|-----------|------------|
| Input | Unsorted array | Sorted array |
| Output | 0-indexed | 1-indexed |
| Best Approach | Hash Map | Two Pointers |
| Time | O(n) | O(n) |
| Space | O(n) | O(1) |
| Space Constraint | None | Must be O(1) |

### Why Two Pointers Work Here:

The sorted array property is crucial:
1. Largest sum possible: `numbers[left] + numbers[right]` (initially)
2. Smallest sum possible: `numbers[left] + numbers[next_left]`
3. Moving pointers guarantees we explore all valid sums efficiently
4. No need to check combinations we've already ruled out

This greedy approach works because sorting ensures we can make optimal decisions at each step.
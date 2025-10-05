from typing import List


def two_sum_two_pointer(nums: List[int], target: int) -> List[int]:
    '''
    Find two indices within nums that add up to target using two-pointer with sorting.
    
    Time: O(n log n), Space: O(n)
    Works on unsorted arrays by sorting first.
    
    Args:
        nums: List of integers (will be sorted internally)
        target: Target sum
        
    Returns:
        List of two 0-indexed positions [i, j] where nums[i] + nums[j] = target
    '''
    
    if not nums or len(nums) < 2 or len(nums) > 10**4:
        raise ValueError("nums must contain between 2 and 10^4 elements inclusive")
    
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    indexed_nums.sort()  # O(n log n)
    
    left = 0
    right = len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            return sorted([indexed_nums[left][1], indexed_nums[right][1]])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    raise ValueError("No solution found")
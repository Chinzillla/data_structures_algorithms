from typing import List

def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
    '''
    Find two indices within nums that add up to target using hash map.
    
    Time: O(n), Space: O(n)
    Works on both sorted and unsorted arrays.
    
    Args:
        nums: List of integers (unsorted or sorted)
        target: Target sum
        
    Returns:
        List of two 0-indexed positions [i, j] where nums[i] + nums[j] = target
    '''

    if not nums or len(nums) < 2 or len(nums) > 10**4:
        raise ValueError("nums must contain between 2 and 10^4 elements inclusive")

    dictionary = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in dictionary:
            return [dictionary[complement], i]
        dictionary[num] = i
        
    raise ValueError("No solution found - violate problem constraints")
    
    
from typing import List

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
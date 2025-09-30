from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums or len(nums) < 2 or len(nums) > 10**4:
            raise ValueError("nums must contain between 2 and 10^4 elements inclusive")

        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0, 1]

        dictionary = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in dictionary:
                return [dictionary[complement], i]
            dictionary[num] = i
            
        raise ValueError("No solution found - violate problem constraints")
    
    
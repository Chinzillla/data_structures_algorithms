from typing import List

def remove_duplicates(nums: List[int]) -> int:
    if (len(nums) < 1 or len(nums) > 3 * 10**4):
        raise ValueError("Incorrect input provided, nums must be between 1 and 3 * 10^4 inclusive")

    if (nums[0] == nums[-1]):
        return 1
    
    last_unique_value = nums[0]
    result = 1

    for i in range(1, len(nums)):
        if nums[i] > 100 or nums[i] < -100:
            raise ValueError("Element is out bounds, must be between -100 and 100 inclusive")
        if nums[i] != last_unique_value:
            nums[result] = nums[i]
            last_unique_value = nums[i]
            result += 1

    return result
    
def main():
    nums1 = [1,1,1,1,1,1,1,1,1]
    nums2 = [1,2,3,4,4,5,6]
    nums3 = [99, 100, 100]
    remove_duplicates(nums1)
    remove_duplicates(nums2)
    remove_duplicates(nums3)

if __name__ == "__main__":
    main()
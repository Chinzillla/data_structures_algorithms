class solution:
    @staticmethod
    def initialize_prefix_arr(nums: list[int]) -> list[int]:
        prefix_sum = [0] * (len(nums) + 1)

        current_sum = 0
        for i in range(1, len(nums) + 1):
            current_sum += nums[i - 1]
            prefix_sum[i] = current_sum

        return prefix_sum
    
    @staticmethod
    def range_sum_query_immutable(nums: list[int], left: int, right: int) -> int:
        prefix_sum = solution.initialize_prefix_arr(nums)
        return prefix_sum[right + 1] - prefix_sum[left]
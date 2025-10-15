from collections import defaultdict
from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Count non-empty submatrices whose sum equals target.
        Uses 2D -> 1D reduction: fix two boundaries on the smaller dimension,
        compress the other dimension into a 1D array of sums, then count
        subarrays equal to target with a prefix-sum frequency map.
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        # Simple prefix sum and target complement search to increment counter
        def count_subarrays_equal_target(arr: List[int]) -> int:
            prefix = 0
            freq = defaultdict(int)
            freq[0] = 1
            count = 0
            for value in arr:
                prefix += value
                count += freq[prefix - target]
                freq[prefix] += 1
            return count

        total_count = 0

        # Square the smaller dimension for better performance
        if rows <= cols:
            # Fix top and bottom rows, compress columns into col_sums
            for top in range(rows):
                col_sums = [0] * cols
                for bottom in range(top, rows):
                    row = matrix[bottom]
                    for c in range(cols):
                        col_sums[c] += row[c]
                    total_count += count_subarrays_equal_target(col_sums)
        else:
            # Fix left and right columns, compress rows into row_sums
            for left in range(cols):
                row_sums = [0] * rows
                for right in range(left, cols):
                    for r in range(rows):
                        row_sums[r] += matrix[r][right]
                    total_count += count_subarrays_equal_target(row_sums)

        return total_count
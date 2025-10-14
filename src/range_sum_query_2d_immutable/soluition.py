from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self._matrix = matrix
            self._prefix = []
            return
        
        self._matrix = matrix
        rows, cols = len(matrix), len(matrix[0])
        # Initialize prefix as (rows+1) x (cols+1) for boundary handling
        self._prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Build full 2D prefix sums (cumulative across rows and columns)
        for i in range(rows):
            for j in range(cols):
                self._prefix[i + 1][j + 1] = (
                    self._prefix[i][j + 1] +      # Above
                    self._prefix[i + 1][j] -      # Left
                    self._prefix[i][j] +          # Subtract overlap
                    matrix[i][j]                  # Current cell
                )
                # print(i,j)
                # print(self._prefix)
                # print("self._prefix[i][j + 1]",self._prefix[i][j + 1])
                # print("self._prefix[i + 1][j]",self._prefix[i + 1][j])
                # print("self._prefix[i][j]",self._prefix[i][j])
                # print("matrix[i][j]",matrix[i][j])
                # print("Result:")
                # print("self._prefix[i + 1][j + 1]",self._prefix[i + 1][j + 1],"=",self._prefix[i][j + 1],"+",self._prefix[i + 1][j],"-",self._prefix[i][j],"+",matrix[i][j],"\n")
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # O(1) query using inclusion-exclusion on 2D prefix sums
        return (
            self._prefix[row2 + 1][col2 + 1] -
            self._prefix[row1][col2 + 1] -
            self._prefix[row2 + 1][col1] +
            self._prefix[row1][col1]
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def backtrack(row: int, col: int, word_index: int) -> bool:
            if word_index == len(word):
                return True
            
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or
                board[row][col] != word[word_index]):
                return False
            
            temp = board[row][col]
            board[row][col] = '#'
            
            found = (backtrack(row - 1, col, word_index + 1) or  # up
                     backtrack(row + 1, col, word_index + 1) or  # down
                     backtrack(row, col - 1, word_index + 1) or  # left
                     backtrack(row, col + 1, word_index + 1))    # right
            
            board[row][col] = temp
            
            return found
        
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        
        return False
#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

from collections import Counter

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        answer = True

        def check_list(l: list[str]) -> bool:
            counter = Counter(l)
            for key in counter:
                if key != "." and counter[key] > 1:
                    return False
            return True

        # check rows
        for row in board:
            answer = answer and check_list(row)
        
        # check columns
        for i in range(9):
            column = [row[i] for row in board]
            answer = answer and check_list(column)
        
        # check 3x3 grids
        for i in range(3):
            for j in range(3):
                square = [row[3*j:3*j+3] for row in board[3*i:3*i+3]]
                square = [el for row in square for el in row]
                print(square, i, j)
                answer = answer and check_list(square)

        return answer
        
# @lc code=end


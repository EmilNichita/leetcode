#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        should_zero_first_row = False
        should_zero_first_col = False

        m, n = len(matrix), len(matrix[0])

        # go over the first column
        for i in range(m):
            if matrix[i][0] == 0:
                should_zero_first_col = True
        
        # go over the first row
        for j in range(n):
            if matrix[0][j] == 0:
                should_zero_first_row = True

        # go over each row and column, tracking the zeros by the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # go over the first row and col, zero out the relevant cells
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
         
        if should_zero_first_row:
            for j in range(n):
                matrix[0][j] = 0
        
        if should_zero_first_col:
            for i in range(m):
                matrix[i][0] = 0
        
# @lc code=end


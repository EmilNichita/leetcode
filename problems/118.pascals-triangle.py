#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            new_row = [1] * (i+1)
            for j in range(1, i):
                new_row[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(new_row)
        
        return ans
            
# @lc code=end


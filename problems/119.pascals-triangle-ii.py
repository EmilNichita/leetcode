#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        curr_row = [1, 1]

        for i in range(2, rowIndex+1):
            new_row = [1] * (i+1)
            for j in range(1, i):
                new_row[j] = curr_row[j-1] + curr_row[j]
            curr_row = new_row
        
        return curr_row
# @lc code=end


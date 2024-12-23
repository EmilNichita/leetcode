#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
   def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right = right & (right-1)
        return right & left
        
# @lc code=end


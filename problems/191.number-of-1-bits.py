#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_rep = []
        
        while n>0:
            bit_rep.append(n%2)
            n = n // 2
        
        return sum(bit_rep)
# @lc code=end


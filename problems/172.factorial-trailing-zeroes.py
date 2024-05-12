#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_fives = 0
        curr_five_pow = 5

        while curr_five_pow <= n:
            num_fives += n // curr_five_pow
            curr_five_pow *= 5
        
        return num_fives
        
# @lc code=end


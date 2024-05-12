#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0  
        twos = 0  

        for num in nums:

            twos |= ones & num
            ones ^= num
            
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes

        return ones
        
# @lc code=end


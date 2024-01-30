#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [None] * n
        prefix_prod, postfix_prod = 1, 1

        for i in range(n):
            answer[i] = prefix_prod
            prefix_prod *= nums[i]
        for i in range(n-1, -1, -1):
            answer[i] *= postfix_prod
            postfix_prod *= nums[i]
        
        return answer
# @lc code=end


#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] - max you can rob by house k
        
        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in nums]
       
        for i, n in enumerate(nums):
            if i == 0:
                dp[i] = nums[0]
            elif i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2]+n)
        return dp[-1]
        
# @lc code=end


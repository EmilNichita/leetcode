#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        mask = [False] * n
        mask[0] = True

        for i in range(n):
            for j in range(1, nums[i]+1):
                if i+j < n:
                    mask[i+j] = mask[i] or mask[i+j]
                if mask[-1]:
                    return True

        return mask[-1]
# @lc code=end


#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        mask = [-1] * n
        mask[0] = 0

        for i in range(n):
            for j in range(1, nums[i]+1):
                if i+j < n:
                    mask[i+j] = 1+mask[i] if mask[i+j] == -1 else min(mask[i+j], 1+mask[i])

        return mask[-1]
# @lc code=end


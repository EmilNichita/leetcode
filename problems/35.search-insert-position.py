#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l<r:
            m = (r+l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m
            else:
                l = m+1
        if nums[m] < target:
            return m+1
        return m


# @lc code=end


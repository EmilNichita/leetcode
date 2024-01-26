#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return len(nums)
        
        last_idx = 1
        for i in range(2, len(nums)):
            if nums[i] == nums[last_idx-1] and nums[i] == nums[last_idx]:
                continue
            else:
                last_idx += 1
                nums[last_idx] = nums[i]
        
        return last_idx+1

# @lc code=end


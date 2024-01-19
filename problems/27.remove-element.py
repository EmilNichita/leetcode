#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        last_idx = 0

        for i in range(0, len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[last_idx] = nums[i]
                last_idx += 1
        
        return last_idx
# @lc code=end


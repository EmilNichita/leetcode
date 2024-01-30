#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapped_nums = [nums[(i-k) % len(nums)] for i in range(len(nums))]
        for i in range(len(nums)):
            nums[i] = swapped_nums[i]
# @lc code=end


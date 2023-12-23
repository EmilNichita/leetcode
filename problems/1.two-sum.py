#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap where keys are numbers from nums, and values are their index in nums
        d = {}

        for i, x in enumerate(nums):
            if target-x in d:
                return [i, d[target-x]]
            else:
                d[x] = i
        
        
# @lc code=end

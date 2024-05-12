#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        i = 0
        while i < len(nums):
            first = nums[i]
            curr = first
            while i+1 < len(nums) and nums[i+1] == nums[i]+1:
                i+=1
                curr += 1
            if first == curr:
                result.append(str(first))
            else:
                result.append(f"{first}->{curr}")
            i+=1
        return result
# @lc code=end


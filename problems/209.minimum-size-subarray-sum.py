#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i, j, n = 0, 0, len(nums)
        current_sum = 0
        best_width = n+2

        while i<n:
            while current_sum < target and j<n:
                current_sum+=nums[j]
                j+=1
            if current_sum >= target:
                best_width = min(best_width, j-i)
            current_sum -=nums[i]
            i+=1
        
        return best_width if best_width!= n+2 else 0

# @lc code=end


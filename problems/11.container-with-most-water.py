#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:

        # move with two pointers
        left, right = 0, len(height)-1
        max_vol = 0

        while left < right:
            curr_vol = min(height[left], height[right]) * (right-left)
            max_vol = max(max_vol, curr_vol)

            # the smallest of the bars will never make more volume as
            # we're decreasing the width, so we can safely skip over it
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_vol

# @lc code=end


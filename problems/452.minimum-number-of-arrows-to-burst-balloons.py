#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # start by sorting the list
        points.sort()

        arrows = 0
        current_arrow = points[-1][0]

        # start shooting at the end
        for left, right in points[::-1]:
            if current_arrow > right:
                current_arrow = left
                arrows += 1
        
        return arrows + 1
# @lc code=end


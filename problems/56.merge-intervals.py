#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
            else:
                result.append(interval)
        return result
# @lc code=end


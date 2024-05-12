#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals + [newInterval])
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
            else:
                result.append(interval)
        return result
# @lc code=end


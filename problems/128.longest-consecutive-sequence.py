#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set()
        max_size = 0
        for n in nums:
            m.add(n)
        for n in nums:
            if n-1 in m:
                continue
            else:
                curr = n
                curr_streak = 0
                while curr in m:
                    curr_streak += 1
                    curr += 1
                max_size = max(max_size, curr_streak)
        return max_size
        
# @lc code=end


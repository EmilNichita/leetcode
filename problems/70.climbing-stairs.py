#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2}

        for i in range(1, n+1):
            if i in cache:
                pass
            else:
                cache[i] = cache[i-1] + cache[i-2]
        return cache[n]
# @lc code=end


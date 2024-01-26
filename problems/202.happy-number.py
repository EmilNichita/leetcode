#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        numbers_seen = set()

        while n != 1:

            n = str(n)
            n = [int(c) for c in n]
            n = [x**2 for x in n]
            n = sum(n)

            if n in numbers_seen:
                return False
            
            numbers_seen.add(n)
        
        return True

# @lc code=end


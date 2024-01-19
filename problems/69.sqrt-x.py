#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        l, r = 0, x
        while l<r:
            m = (l+r) // 2
            mm = m * m

            if mm == x:
                return m
            if mm < x:
                l = m+1
            else:
                r = m
        
        if m*m > x:
            return m-1
        return m

# @lc code=end


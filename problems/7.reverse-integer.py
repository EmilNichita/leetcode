#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # operate on strings
        s = str(x)
        
        # keep a flag for the minus, then strip it out 
        minus_flag = x < 0
        if minus_flag:
            s = s[1:]
        
        s_reversed = s[::-1]
        x_reversed = int(s_reversed)

        # add the minus back if needed
        x_reversed = -x_reversed if minus_flag else x_reversed

        # check the bounds before returning
        return x_reversed if (x_reversed >= -2**31 and x_reversed < 2**31) else 0
        
# @lc code=end


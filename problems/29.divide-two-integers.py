#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == 0:
            return 0

        initial_minus = (dividend < 0 and divisor > 0) \
            or (dividend > 0 and divisor < 0)
        
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor

        whole_part = 0
        while dividend >= divisor:
            dividend -= divisor
            whole_part += 1
        
        whole_part = -whole_part if initial_minus else whole_part

        whole_part = min(whole_part, 2**31 -1)
        whole_part = max(whole_part, -(2**31))

        return whole_part

# @lc code=end


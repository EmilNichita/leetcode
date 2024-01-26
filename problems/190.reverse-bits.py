#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        bit_rep = []
        
        while n>0:
            bit_rep.append(n%2)
            n = n // 2
        
        for _ in range(len(bit_rep), 32):
            bit_rep.append(0)
        
        result, curr_exponent = 0, 1
        bit_rep = bit_rep[::-1]

        for b in bit_rep:
            result += curr_exponent * b
            curr_exponent *= 2
        
        return result


# @lc code=end


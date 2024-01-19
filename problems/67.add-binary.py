#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        i, j = len(a) - 1, len(b) - 1
        carry = 0

        while i>= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res.append(str(carry%2))
            carry = carry // 2
        
        return "".join(res[::-1])
            
# @lc code=end


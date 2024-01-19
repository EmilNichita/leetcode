#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            carry = 0
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
        
        if carry == 1:
            digits = [1] + digits
        
        return digits
# @lc code=end


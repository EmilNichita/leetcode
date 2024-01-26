#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        result = []

        n = columnNumber

        while n > 0:
            n -= 1
            letter = letters[n % 26]
            result.append(letter)
            n = n // 26
        
        return "".join(result[::-1])
            
# @lc code=end


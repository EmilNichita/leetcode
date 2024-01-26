#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res, curr_factor = 0, 1

        for c in columnTitle[::-1]:
            n = ord(c) - ord('A') + 1
            res += n * curr_factor
            curr_factor *= 26
        
        return res

# @lc code=end


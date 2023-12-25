#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,            
        }

        n = 0
        max_val_found = -1

        # go through each char from the end
        # letters that are before bigger ones are with minus
        for c in s[::-1]:
            if values[c] >= max_val_found:
                n += values[c]
            else:
                n -= values[c]
            max_val_found = max(max_val_found, values[c])
        return n
        
# @lc code=end


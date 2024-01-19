#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = []
        
        # find the last character location
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                continue
            else:
                break
        
        while i>=0 and s[i] != " ":
            result.append(s[i])
            i -= 1
        
        return len(result)
        
            
# @lc code=end


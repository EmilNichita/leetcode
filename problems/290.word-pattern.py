#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False
        
        for c, word in zip(pattern, words):
            if c in d:
                if d[c] != word:
                    return False
            else:
                d[c] = word
        
        return len(set(d.values())) == len(d)
# @lc code=end


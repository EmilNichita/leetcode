#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

from collections import Counter
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        t_counter = Counter(t)

        if set(s_counter.keys()) != set(t_counter.keys()):
            return False
        
        for key in s_counter:
            if s_counter[key] != t_counter[key]:
                return False
        
        return True
# @lc code=end


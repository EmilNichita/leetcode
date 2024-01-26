#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}

        if len(s) != len(t):
            return False
        
        for x, y in zip(s, t):
            if x in mapping:
                if y != mapping[x]:
                    return False
            else:
                mapping[x] = y
        
        return len(set(mapping.values())) == len(mapping)

# @lc code=end


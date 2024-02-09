#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        s_idx = 0
        for t_idx in range(len(t)):
            if s_idx == len(s):
                return True
            else:
                if s[s_idx] == t[t_idx]:
                    s_idx += 1
        
        return s_idx == len(s)
# @lc code=end


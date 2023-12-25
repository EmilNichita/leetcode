#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = []
        should_stop = False

        # for each i, check the i-th letter for each string
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    should_stop = True
            if should_stop:
                break
            else:
                result.append(strs[0][i])
        
        return "".join(result)

# @lc code=end


#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle) + 1):
            for j in range(len(needle)+1):
                if j==len(needle):
                    return i
                if haystack[i+j] != needle[j]:
                    break
                
        return -1
# @lc code=end


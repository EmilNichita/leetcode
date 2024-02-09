#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = []

        n = len(s)
        i = 0
        while i < n:
            if s[i] == " ":
                i+=1
            else:
                j = i+1
                while j<n and s[j] != " ":
                    j+=1
                words.append(s[i:j])
                i = j
        
        return " ".join(words[::-1])

# @lc code=end


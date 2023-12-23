#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        n = len(s)
        hashset = set()

        if n < 2:
            return n
        
        left, right = 0, 1
        hashset.add(s[0])
        
        while right < n:
            if s[right] not in hashset:
                hashset.add(s[right])
                right += 1
                max_size = max(max_size, len(hashset))
            else:
                hashset.remove(s[left])
                left += 1
        
        return max_size

# @lc code=end


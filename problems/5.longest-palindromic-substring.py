#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # implementation of the Manacher's Algorithm
        # we first expand the string, inserting #'s between each character

        modified_s = "#" + "#".join(s) + "#"
        n = len(modified_s)

        # array storing the max palindrome length at each char
        P = [0] * n
        
        # center and right boundary of the current palindrome
        C, R = 0, 0  

        # max values found so far
        max_len, max_center = 0, 0

        # go through each char
        for i in range(n):

            # if i is in [C, R), we know its mirror
            # found at 2*C - i already has a max palindrome value
            # found, from which we can start
            # we're limited by R - i
            if i < R:
                P[i] = min(R - i, P[2*C - i])

            # check the max size of the palindrome at this location
            a, b = i - (1 + P[i]), i + (1 + P[i])
            while a >= 0 and b < n and modified_s[a] == modified_s[b]:
                P[i] += 1
                a -= 1
                b += 1

            # if we passed the current palindrome's boundary, update it
            if i + P[i] > R:
                C, R = i, i + P[i]

            # update the max values if needed
            if P[i] > max_len:
                max_len = P[i]
                max_center = i

        # return the palindrome for the original string
        start = (max_center - max_len) // 2
        end = start + max_len
        return s[start:end]
# @lc code=end


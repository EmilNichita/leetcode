#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n_p, n_s = len(p), len(s)
        
        # [len(s)+1,  len(p)+1] table, where dp[i,j] = s[:i] matches p[:j]
        dp = [[False] * (n_p + 1) for _ in range(n_s + 1)]

        # empty string matches empty pattern
        dp[0][0] = True

        # when s is empty, p matches it only if it's of the form a*b*c*...
        # as a consequence, dp[0][1] is always false (we can't have a starting * in p)
        for i in range(2, n_p+1):
            dp[0][i] = dp[0][i-2] and p[i-1] == '*'

        # fill the table, rows first (increasing prefixes of s)
        for i in range(1, n_s + 1):
            for j in range(1, n_p + 1):
                # last element in pattern not a star
                if p[j-1] != "*":
                    # s[:i] matches p[:j] if s[:(i-1)] matches p[:(j-1)] and p[j-1] matches s[i-1] 
                    dp[i][j] = dp[i-1][j-1] and p[j-1] in [s[i-1], "."]
                else:
                    # p[j-1] is a star
                    # if without the star, or using the star to delete the j-2'th pattern element
                    # we have a match, then we have one with the star too
                    dp[i][j] = dp[i][j-2] or dp[i][j-1]

                    # we can also use the j-2'th pattern element for the i-1'th string one,
                    # if s[:i-1] matches p[:j]
                    if p[j-2] in [s[i-1], "."]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        
        return dp[-1][-1]

# @lc code=end


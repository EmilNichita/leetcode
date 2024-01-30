#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations, reverse=True)

        return sum([i<j for i, j in enumerate(sorted_citations)])
# @lc code=end


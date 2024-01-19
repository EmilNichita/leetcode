#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        lowest = prices[0]
        highest_after = prices[0]

        for p in prices:
            if p < lowest:
                lowest = p
                highest_after = p
            if highest_after < p:
                highest_after = p
        
        return max(0, highest_after-lowest)

# @lc code=end


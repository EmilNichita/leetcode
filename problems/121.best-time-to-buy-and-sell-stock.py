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

        buy, sell = 0, 1
        max_profit = 0

        while sell < len(prices):
            curr_profit = prices[sell] - prices[buy]

            if prices[buy] < prices[sell]:
                max_profit = max(curr_profit, max_profit)
            else:
                buy = sell
            sell += 1

        return max_profit

# @lc code=end


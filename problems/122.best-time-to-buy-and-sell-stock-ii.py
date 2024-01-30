#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy, sell = 0, 0

        day = 0
        while day < len(prices) -1:
            
            # find the day to buy - the smallest one continuously
            while day < len(prices)-1 and prices[day] >= prices[day+1]:
                day += 1
            buy = day

            while day < len(prices)-1 and prices[day] <= prices[day+1]:
                day += 1
            sell = day
            
            profit += prices[sell] - prices[buy]

        return profit

# @lc code=end


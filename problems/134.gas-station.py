#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start, surplus, max_surplus, n = 0, 0, 0, len(gas)

        for i in range(n):
            max_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]

            if surplus < 0:
                surplus = 0
                start = i+1
        
        return -1 if (max_surplus<0) else start

# @lc code=end


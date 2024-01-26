#
# @lc app=leetcode id=2965 lang=python3
#
# [2965] Find Missing and Repeated Values
#

# @lc code=start
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        occurences = {}
        for l in grid:
            for el in l:
                if el in occurences:
                    occurences[el] += 1
                else:
                    occurences[el] = 1
        
        results = [0, 0]

        for i in range(1, len(grid) * len(grid)+1):
            if i not in occurences:
                results[1] = i
            elif occurences[i] == 2:
                results[0] = i
        
        return results
# @lc code=end


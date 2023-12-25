#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        n = len(s)
        
        # list of rows that will be populated
        result = [list() for _ in range(numRows)]

        i = 0
        while i < n:
            # going vertically down, adding to each row  
            for k in range(numRows):
                if i<n:
                    result[k].append(s[i])
                    i+=1
            
            # going up, adding to each row
            for k in range(numRows-2, 0, -1):
                if i<n:
                    result[k].append(s[i])
                    i+=1
        
        # concatenate each row, then all rows
        return "".join(["".join(x) for x in result])


            
# @lc code=end


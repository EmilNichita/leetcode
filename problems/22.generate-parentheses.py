#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.recursive(n, res, 0, "", 0)
        return res

    def recursive(self, n, res, index, curr_string, curr_open_count):
        if index == 2*n:
            res.append(curr_string)
            return
        
        if curr_open_count < 2*n - index:
            self.recursive(n, res, index+1, curr_string+"(", curr_open_count+1)
        if curr_open_count > 0:
            self.recursive(n, res, index+1, curr_string+")", curr_open_count-1)
        
# @lc code=end


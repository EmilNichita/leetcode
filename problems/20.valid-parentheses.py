#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ']': '[',
            ')': '(',
            '}': '{',
        }

        for c in s:
            if c in ['[', '(', '{']:
                stack.append(c)
                continue
            
            if len(stack) == 0:
                return False
            
            if stack[-1] == pairs[c]:
                stack.pop(-1)
                continue
            else:
                return False
        
        return len(stack) == 0
                
# @lc code=end


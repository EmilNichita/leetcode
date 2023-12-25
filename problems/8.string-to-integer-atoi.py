#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # remove leading whitespaces
        s = s.lstrip()

        if not s:
            return 0

        # check the sign if needed
        minus_flag = s[0] == "-"
        if s[0] in ["+", "-"]:
            s = s[1:]
        
        # read continuous digits, add them to a list we'll transform in an int
        digit_set = {str(x) for x in range(10)}
        digit_list = [] 
        i = 0
        while i < len(s):
            if s[i] in digit_set:
                digit_list.append(s[i])
            else:
                break
            i+=1
        
        # if we didn't find any digit, return 0 - although debatable
        if not digit_list:
            return 0
        
        # generate the in from the string
        x = int("".join(digit_list))

        # account for the minus
        x = -x if minus_flag else x

        x = max(-2**31, x)
        x = min(2**31 - 1, x)

        return x
        
# @lc code=end


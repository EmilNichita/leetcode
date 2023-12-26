#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"], 
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        res = []

        if len(digits) == 0:
            return []
        
        self.f(digits, 0, "", res, mapping)
        return res

    def f(self, digits, index, current_word, res, mapping):
        if index == len(digits):
            res.append(current_word)
            return
        
        for i in mapping[int(digits[index])]:
            self.f(digits, index+1, current_word+i, res, mapping)
                    
# @lc code=end


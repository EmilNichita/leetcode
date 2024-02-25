#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        for key in ransomCounter:
            if key not in magazineCounter or ransomCounter[key] > magazineCounter[key]:
                return False
        
        return True       
# @lc code=end


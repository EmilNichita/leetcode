#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:

    def trap(self, height: List[int]) -> int:

        n = len(height)

        if n <= 2:
            return 0

        total, i, j = 0, 1, n-1

        l, r = height[0], height[-1]

        while i<=j:
            if height[i]>l:
                l = height[i]
            if height[j]>r:
                r = height[j]
            
            if l <=r:
                total += l - height[i]
                i+=1
            else:
                total += r - height[j]
                j -= 1
    
        return total
# @lc code=end


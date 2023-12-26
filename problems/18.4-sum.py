#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        return self.kSum(nums, target, k=4)
    
    def kSum(self, nums, target, k):
        res = []
        n = len(nums)

        if n==0:
            return []
        
        if k==2:
            return self.twoSum(nums, target)
    
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue

            for subset in self.kSum(nums[i+1:], target-nums[i], k-1):
                res.append([nums[i]] + subset)
        
        return res
    
    def twoSum(self, nums, target):
        res = []
        l, r = 0, len(nums) - 1

        while (l < r):
            curr_sum = nums[l] + nums[r]
            if curr_sum < target or (l > 0 and nums[l] == nums[l - 1]):
                l += 1
            elif curr_sum > target or (r < len(nums) - 1 and nums[r] == nums[r + 1]):
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
                                                        
        return res

# @lc code=end


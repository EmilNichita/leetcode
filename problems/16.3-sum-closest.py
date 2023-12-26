#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        result = nums[0] + nums[1] + nums[2]
        
        for i in range(n-2):
            
            # if we've checked this number before, but with more options
            # for j and k, we might as well skip this one
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, n-1

            while j<k:
                cur_sum = nums[i] + nums[j] + nums[k]

                if cur_sum == target:
                    return target

                if abs(cur_sum - target) < abs(result - target):
                    result = cur_sum
                
                if cur_sum < target:
                    j+=1
                else:
                    k-=1
        
        return result
                

# @lc code=end


#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort the input
        nums.sort()
        result = []

        n = len(nums)

        # go through each number, try to find unique pairs that 
        # when added to it make 0
        for i in range(n):
            # skip duplicates forward
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            # search with two pointers
            # to avoid duplicates, start from the right of i
            l, r = i+1, n-1

            while l<r:
                s = nums[l] + nums[i] + nums[r]

                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    result.append([nums[l], nums[i], nums[r]])
                    l+=1
                    # again, move l to avoid duplicates
                    while nums[l-1] == nums[l] and l<r:
                        l+=1
        
        return result
# @lc code=end


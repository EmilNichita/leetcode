#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_lead = 1
        current_leader = nums[0]

        for n in nums[1:]:
            if n == current_leader:
                current_lead += 1
            else:
                if current_lead == 0:
                    current_lead = 1
                    current_leader = n
                else:
                    current_lead -= 1
        
        return current_leader

# @lc code=end


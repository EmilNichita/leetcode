#
# @lc app=leetcode id=2960 lang=python3
#
# [2960] Count Tested Devices After Test Operations
#

# @lc code=start
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        curr_percentage_to_drop = 0
        devices_tested = 0
        for battery in batteryPercentages:
            battery -= curr_percentage_to_drop
            if battery > 0:
                devices_tested += 1
                curr_percentage_to_drop += 1
        
        return devices_tested
# @lc code=end


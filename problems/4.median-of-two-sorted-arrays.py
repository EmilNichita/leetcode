#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)

        # make sure nums1 is the smaller of the two
        if n1 > n2: 
            return self.findMedianSortedArrays(nums2, nums1)
        
        # the median will split each array in two halves:
        # left_half_nums1 <= median <= right_half_nums1
        # left_half_nums2 <= median <= right_half_nums2
        # such that len(left_half_nums1) + len(left_half_nums2) ~ (len(num1) + len(nums2)) / 2
        # we can do a binary search to find the halves in nums1, as the comment above means the
        # halves in nums2 are implicit. we just need to check the two conditions then

        n = n1 + n2
        n_half = (n+1) // 2

        # binry search index for nums1
        right = 0
        left = n1

        while right<=left:
            mid_n1 = (right + left) // 2
            mid_n2 = n_half - mid_n1

            l1 = float('-inf') if mid_n1<=0 else nums1[mid_n1-1]
            l2 = float('-inf') if mid_n2<=0 else nums2[mid_n2-1]
            r1 = float('inf') if mid_n1>=n1 else nums1[mid_n1]
            r2 = float('inf') if mid_n2>=n2 else nums2[mid_n2]

            if l1 <= r2 and l2 <= r1:
                if n%2 == 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                left = mid_n1 - 1
            else:
                right = mid_n1 + 1
        
        return 0

# @lc code=end


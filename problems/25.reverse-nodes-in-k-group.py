#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # baseline - if we have less than k remaining nodes, return the list as is
        curr = head
        for _ in range(k):
            if curr is None:
                return head
            curr = curr.next

        prev = None
        curr = head
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head.next = self.reverseKGroup(curr, k)

        return prev        
# @lc code=end


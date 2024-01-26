#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        if head is None:
            return head

        curr, prev = head, dummy

        while curr.next is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        curr.next = prev
        head.next = None

        return curr
# @lc code=end


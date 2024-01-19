#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cache = set()
        if head is None:
            return None
        curr = ListNode()
        curr.next = head
        while curr is not None and curr.next is not None:
            if curr.next.val not in cache:
                cache.add(curr.next.val)
                curr = curr.next
            else:
                curr.next = curr.next.next
        return head

# @lc code=end


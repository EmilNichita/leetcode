#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        for _ in range(n+1):
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
        
        deleted_node = slow.next
        slow.next = slow.next.next

        del deleted_node

        return dummy.next
# @lc code=end


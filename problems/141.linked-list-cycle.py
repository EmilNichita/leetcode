#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        slow, fast = head, head.next

        while fast is not None:
            if fast.next is None or fast.next.next is None:
                return False
            
            if slow is fast:
                return True
            
            slow = slow.next
            fast = fast.next.next
        return False
# @lc code=end


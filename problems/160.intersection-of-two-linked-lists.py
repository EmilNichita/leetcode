#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # get lengths of A and B
        n_a, n_b = self.get_length(headA), self.get_length(headB)

        while n_a > n_b:
            headA = headA.next
            n_a -= 1

        while n_b > n_a:
            headB = headB.next
            n_b -= 1
        
        while headA is not headB:
            headA, headB = headA.next, headB.next
        
        return headA
    
    def get_length(self, head: ListNode) -> int:
        if head is None:
            return 0
        
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        
        return length
# @lc code=end


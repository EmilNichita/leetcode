#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
           return 0
        
        # dummy front node, removed later
        dummy_root = ListNode()
        curr_node = dummy_root
        
        carry = 0
        
        while l1 is not None or l2 is not None or carry>0:
            
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            curr_sum = l1_val + l2_val + carry
            curr_digit, carry = curr_sum % 10, curr_sum // 10

            new_node = ListNode(curr_digit)
            curr_node.next = new_node
            curr_node = new_node

            # move to the right in each list if possible
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        result = dummy_root.next
        del dummy_root
        return result
        
# @lc code=end


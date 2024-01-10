#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeSort(lists, 0, len(lists)-1)
    
    def mergeSort(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = start + (end - start) // 2
        left = self.mergeSort(lists, start, mid)
        right = self.mergeSort(lists, mid+1, end)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy_node = ListNode()
        current_node = dummy_node

        while left and right:
            if left.val <= right.val:
                current_node.next = left
                current_node = current_node.next
                left = left.next
            else:
                current_node.next = right
                current_node = current_node.next
                right = right.next
        
        while left:
            current_node.next = left
            current_node = current_node.next
            left = left.next
        
        while right:
            current_node.next = right
            current_node = current_node.next
            right = right.next
        
        return dummy_node.next

# @lc code=end


#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = []

        if root is None:
            return True
        
        stack.append([root.left, root.right])

        while len(stack) > 0:
            left, right = stack.pop()

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])
        
        return True
        


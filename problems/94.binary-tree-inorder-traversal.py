#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversalIterative(root)
    
    def inorderTraversalRecursive(self, root):
        if root is None:
            return []
        return self.inorderTraversalRecursive(root.left) + [root.val] + self.inorderTraversalRecursive(root.right)

# @lc code=end


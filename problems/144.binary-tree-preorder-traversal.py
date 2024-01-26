#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.recursive_traversal(root)
    
    def recursive_traversal(self, root: TreeNode):
        result = []

        if root is not None:
            result.append(root.val)
        else:
            return []
        
        result += self.recursive_traversal(root.left)
        result += self.recursive_traversal(root.right)

        return result

# @lc code=end


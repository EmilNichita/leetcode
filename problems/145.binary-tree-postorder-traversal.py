#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.recursive_traversal(root)
    
    def recursive_traversal(self, root: TreeNode):
        result = []

        if root is None:
            return []
        
        result += self.recursive_traversal(root.left)
        result += self.recursive_traversal(root.right)

        result.append(root.val)            

        return result
# @lc code=end


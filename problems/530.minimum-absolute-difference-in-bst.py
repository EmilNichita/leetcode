#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        # get the sorted array from the BST by doing inorder traversal
        sorted_arr = self.inorder_traverse(root)
        
        # find the min difference of adjacent values in the sorted array
        min_diff = min([abs(x - y) for x, y in zip(sorted_arr[:-1], sorted_arr[1:])])

        return min_diff
    
    def inorder_traverse(self, node):

        return ([] if node.left is None else self.inorder_traverse(node.left)) + \
        [node.val] + ([] if node.right is None else self.inorder_traverse(node.right))
         
# @lc code=end


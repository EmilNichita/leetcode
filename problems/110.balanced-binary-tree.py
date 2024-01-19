#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0
    
    def height(self, root) -> int:
        if not root:
            return 0
        l, r = self.height(root.left), self.height(root.right)

        if -1 in [l, r] or abs(l-r)>1:
            return -1
        
        else:
            return 1+max(l, r)
            

# @lc code=end


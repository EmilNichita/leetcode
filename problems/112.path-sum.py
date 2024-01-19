#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(node):
            return node is not None and node.right is None and node.left is None
        
        if root is None:
            return False

        stack = [(root, root.val)]

        while len(stack) > 0:
            curr, curr_sum = stack.pop()
            if curr_sum == targetSum and is_leaf(curr):
                return True
            else:
                if curr.left is not None:
                    stack.append((curr.left, curr.left.val + curr_sum))
                if curr.right is not None:
                    stack.append((curr.right, curr.right.val + curr_sum))
        
        return False

# @lc code=end


#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_found = 1
        while len(stack) > 0:
            curr, depth = stack.pop()
            if curr:
                max_found = max(max_found, depth)
                stack.append((curr.left, depth+1))
                stack.append((curr.right,depth+1))
        return max_found


# @lc code=end


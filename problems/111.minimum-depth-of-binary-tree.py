#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = [(root, 1)]

        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        while len(queue) > 0:
            curr, depth = queue.pop(0)
            if is_leaf(curr):
                return depth
            else:
                if curr:
                    queue.append((curr.left, depth+1))
                    queue.append((curr.right, depth+1))
        
        return 0



# @lc code=end


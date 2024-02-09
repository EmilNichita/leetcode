#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [(root, 0)]
        result = {}

        while queue!=[]:
            node, level = queue.pop(0)
            if level in result:
                result[level] = (result[level][0]+1, result[level][1]+node.val)
            else:
                result[level] = (1, node.val)

            if node.left is not None:
                queue.append((node.left, level+1))
            
            if node.right is not None:
                queue.append((node.right, level+1))

        result = [result[x][1] / result[x][0] for x in range(len(result))]
        return result

# @lc code=end


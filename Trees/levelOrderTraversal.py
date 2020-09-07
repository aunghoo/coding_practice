''' Medium
https://leetcode.com/problems/binary-tree-level-order-traversal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        traversed = []
        while queue:
            traversed.append([])
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if not node:
                    continue
                traversed[-1].append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if not traversed[-1]:
                traversed.pop(-1)
        return traversed
''' Hard
https://leetcode.com/problems/binary-tree-maximum-path-sum
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return max(self.getBestSums(root))

    def getBestSums(self, root):
        if not root:
            return (-math.inf, -math.inf)

        leftNoRoot, leftCanAddRoot = self.getBestSums(root.left)
        rightNoRoot, rightCanAddRoot = self.getBestSums(root.right)

        # first choice is parent cannot add your path
        noParent = max(leftCanAddRoot+root.val+rightCanAddRoot, leftNoRoot, rightNoRoot, leftCanAddRoot, rightCanAddRoot)

        # second choice allows parent to add more
        canAddParent = max(leftCanAddRoot + root.val, rightCanAddRoot + root.val, root.val)

        return (noParent, canAddParent)
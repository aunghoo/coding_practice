''' Medium
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''
import collections

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        stack = collections.deque()
        nodes = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            nodes.append(cur.val)
            cur = cur.right
        return nodes

# recursive solution: simple
def traverseRecursive(root, nodes):
    if not root:
        return
    traverseRecursive(root.left, nodes)
    nodes.append(root.val)
    traverseRecursive(root.right, nodes)

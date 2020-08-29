''' Medium
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''

import collections
import copy

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        zigzagNodes = []
        currentLevelStack = collections.deque()
        nextLevelStack = collections.deque()
        currentLevelStack.append(root)
        leftToRight = True
        level = []
        while currentLevelStack or nextLevelStack:
            # after each level, switch stacks
            if not currentLevelStack:
                currentLevelStack = copy.copy(nextLevelStack)
                nextLevelStack.clear()
                leftToRight = False if leftToRight else True
                zigzagNodes.append(level)
                level = []
            cur = currentLevelStack.pop()
            level.append(cur.val)
            if leftToRight:
                if cur.left:
                    nextLevelStack.append(cur.left)
                if cur.right:
                    nextLevelStack.append(cur.right)
            else:
                if cur.right:
                    nextLevelStack.append(cur.right)
                if cur.left:
                    nextLevelStack.append(cur.left)
        zigzagNodes.append(level)
        return zigzagNodes

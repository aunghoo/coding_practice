''' Medium
https://leetcode.com/problems/validate-binary-search-tree/
'''

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return isValidHelper(root, float('-inf'), float('inf'))

def isValidHelper(root, lower, upper):
    if not root:
        return True
    if root.val <= lower or root.val >= upper:
        return False
    return isValidHelper(root.left, lower, root.val) and isValidHelper(root.right, root.val, upper)

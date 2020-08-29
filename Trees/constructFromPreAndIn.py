''' Medium
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        order(root, preorder, inorder)
        return root

def order(node, preorder, inorder):
    if not preorder:
        return
    index = inorder.index(node.val)
    leftIn = inorder[:index]
    rightIn = inorder[index+1:] # does not go out of index

    leftPre = []
    if leftIn:
        leftPre = preorder[1:index+1]

    #set left
    if len(leftPre) > 0:
        node.left = TreeNode(preorder[1])
    order(node.left, leftPre, leftIn)

    rightPre = preorder[index+1:]
    #set right
    if index+1 < len(preorder):
        node.right = TreeNode(preorder[index+1])
    order(node.right, rightPre, rightIn)

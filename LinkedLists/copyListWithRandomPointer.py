''' Medium
https://leetcode.com/problems/copy-list-with-random-pointer/
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        copyList = Node(0, None, None)
        copyNode = copyList
        addressMap = {} # addresses of list and their indices
        copyListAddresses = [] # addresses of the copy list nodes
        node = head
        index = 0
        while(node):
            copyNode.next = Node(node.val, None, None)
            addressMap[node] = index
            copyListAddresses.append(copyNode.next)
            node = node.next
            copyNode = copyNode.next
            index += 1

        # get the index of nodes random pointers point to
        randomPointers = []
        node = head
        while(node):
            if not node.random:
                randomPointers.append(-1)
            else:
                randomPointers.append(addressMap[node.random])
            node = node.next

        copyList = copyList.next #correct to actual head
        copyNode = copyList
        index = 0
        for c in copyListAddresses:
            r = randomPointers[index]
            if r == -1:
                c.random = None
            else:
                c.random = copyListAddresses[r]
            index += 1

        return copyList

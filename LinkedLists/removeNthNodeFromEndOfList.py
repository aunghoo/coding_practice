''' Medium
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        firstPtr = head
        secondPtr = head
        prevPtr = head
        for i in range(n-1):
            secondPtr = secondPtr.next
        while secondPtr.next:
            prevPtr = firstPtr
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next
        if prevPtr == firstPtr:
            return firstPtr.next if firstPtr.next else None
        prevPtr.next = firstPtr.next
        firstPtr = None
        return head

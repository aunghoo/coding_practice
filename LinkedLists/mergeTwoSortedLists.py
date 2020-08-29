''' Easy <good for linked list revision>
https://leetcode.com/problems/merge-two-sorted-lists
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstPtr = l1
        secondPtr = l2
        mergedList = None
        head = None
        if not firstPtr and not secondPtr:
            return None
        if not firstPtr:
            return secondPtr
        if not secondPtr:
            return firstPtr
        if firstPtr.val > secondPtr.val:
            head = ListNode(secondPtr.val)
            mergedList = head
            secondPtr = secondPtr.next
        else:
            head = ListNode(firstPtr.val)
            mergedList = head
            firstPtr = firstPtr.next
        while firstPtr and secondPtr:
            if firstPtr.val > secondPtr.val:
                mergedList.next = ListNode(secondPtr.val)
                mergedList = mergedList.next
                secondPtr = secondPtr.next
            else:
                mergedList.next = ListNode(firstPtr.val)
                mergedList = mergedList.next
                firstPtr = firstPtr.next
        if firstPtr:
            mergedList.next = firstPtr
        else:
            mergedList.next = secondPtr
        return head

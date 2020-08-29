''' Easy
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = 0
        slow = 0
        ended = False
        while fast < len(nums):
            while nums[fast] == nums[slow]:
                fast += 1
                if fast == len(nums):
                    ended = True
                    break
            slow += 1
            if not ended:
                nums[slow] = nums[fast]
        nums = nums[:slow]
        return slow

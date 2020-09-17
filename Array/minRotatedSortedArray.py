''' Medium
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Test cases:
        # 6,1,2,3,4,5
        # 6,7,8,9,1,2
        l, r = 0, len(nums)
        while(l < r):
            mid = int((l+r)/2)
            # next left is greater than self, then this is pivot
            if mid == 0 or nums[mid-1] > nums[mid]:
                return nums[mid]
            # rotation is on the left
            if nums[mid] < nums[l]:
                r = mid
            # rotation is on the right
            elif nums[mid] > nums[r-1]:
                l = mid + 1
            else:
                return nums[l]
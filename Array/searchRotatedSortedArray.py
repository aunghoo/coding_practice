''' Medium
https://leetcode.com/problems/search-in-rotated-sorted-array/
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while (l < r):
            mid = int((l + r)/2)

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                # if rotation is on right side and target is less than left boundary
                if nums[mid] > nums[r-1] and target < nums[l]:
                    l = mid + 1
                else:
                    r = mid
            else:
                # if rotation is on left side and target is greater than right boundary
                if nums[mid] < nums[l] and target > nums[r-1]:
                    r = mid
                else:
                    l = mid + 1

        return -1
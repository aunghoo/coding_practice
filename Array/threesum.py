''' Medium
https://leetcode.com/problems/3sum
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        # needs to sort the nums to get unique triplets
        nums.sort()
        for i, n in enumerate(nums):
            # we don't want repeated sequences
            if i > 0 and nums[i-1] == n:
                continue
            # search the other two numbers in the three sum
            l, r = i+1, len(nums)-1
            while (l < r):
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    triplets.append([nums[i],nums[l],nums[r]])
                    left = nums[l]
                    while nums[l] == left and l < r:
                        l += 1
        return triplets

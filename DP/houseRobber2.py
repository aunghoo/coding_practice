'''
https://leetcode.com/problems/house-robber-ii/
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        needsAlt = False
        bestWithFirst, adjWithFirst = self.getBest(nums)
        # This means that the last house was robbed (meaning there is a possible cycle)
        # So try again by excluding the very first house
        if bestWithFirst != adjWithFirst:
            slicedNums = nums[1:]
            bestWithoutFirst, adjWithoutFirst = self.getBest(slicedNums)
            return max(bestWithoutFirst, adjWithFirst)
        return bestWithFirst

    def getBest(self, nums):
        prevBest = 0
        adjBest = nums[0]
        needsAlt = False
        for i, n in enumerate(nums[1:]):
            currentBest = max(prevBest + n, adjBest)
            prevBest = adjBest
            adjBest = currentBest
        return adjBest, prevBest
        '''
        2,4,3,5,6
        '''
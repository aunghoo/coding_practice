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
        bestWithFirst = self.getBest(nums[:-1])
        bestWithoutFirst = self.getBest(nums[1:])
        # compare and return the better one
        return max(bestWithFirst, bestWithoutFirst)

    def getBest(self, nums):
        prevBest = 0
        adjBest = nums[0]
        needsAlt = False
        for i, n in enumerate(nums[1:]):
            currentBest = max(prevBest + n, adjBest)
            prevBest = adjBest
            adjBest = currentBest
        return adjBest
        '''
        2,4,3,5,6
        '''
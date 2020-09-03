'''
https://leetcode.com/problems/house-robber
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        adjBest = nums[0]
        prevBest = 0
        for i, n in enumerate(nums[1:]):
            currentBest = max(adjBest, prevBest + n)
            prevBest = adjBest
            adjBest = currentBest
        return adjBest
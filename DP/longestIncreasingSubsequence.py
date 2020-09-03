'''
https://leetcode.com/problems/longest-increasing-subsequence
'''

# O(n^2) solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [[0] * len(nums) for i in range(len(nums))]
        highest_global = 0
        for c in range(len(nums)):
            highest = 1
            for prev in range(c):
                if nums[c] > nums[prev] and mem[prev] + 1 > highest:
                    highest = mem[prev] + 1
            mem[c] = highest
            if highest > highest_global:
                highest_global = highest
        return highest_global


# Needs to figure out O(n log n) Solution
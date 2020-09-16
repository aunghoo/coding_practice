''' Easy
https://leetcode.com/problems/two-sum
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            sub = target - n
            if sub in seen:
                return [seen[sub], i]
            seen[n] = i
        
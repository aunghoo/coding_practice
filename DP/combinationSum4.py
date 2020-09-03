'''
https://leetcode.com/problems/combination-sum-iv
'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = {}
        return self.memoizeCombinationSum4(nums, target, mem)

    def memoizeCombinationSum4(self, nums, target, mem):
        if target == 0:
            return 0
        if target in mem:
            return mem[target]
        combs = 0
        for i, n in enumerate(nums):
            if n == target:
                combs += 1
            elif n < target:
                combs += self.memoizeCombinationSum4(nums, target-n, mem)
        mem[target] = combs
        return combs

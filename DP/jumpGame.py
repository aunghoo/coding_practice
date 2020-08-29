''' Medium
https://leetcode.com/problems/jump-game
'''
#Top down DP solution of jump game
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = {}
        return canReach(nums, 0, mem)

def canReach(nums, i, mem):
    if i in mem:
        return mem[i]
    if i >= len(nums)-1:
        mem[i] = True
        return True
    for j in range(nums[i], 0, -1):
        if canReach(nums, j+i, mem):
            mem[i] = True
            return True
    mem[i] = False
    return False

#Greedy solution of jump game
def greedyReach(nums):
    pos = len(nums) - 1
    for i in range(pos, -1, -1):
        if i + nums[i] >= pos:
            pos = i
    return True if pos == 0 else False

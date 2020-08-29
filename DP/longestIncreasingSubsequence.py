'''
https://leetcode.com/problems/longest-increasing-subsequence
'''

# O(n^2) solution
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        lengths = [1 for i in range(len(nums))]
        for cur in reversed(range(len(nums))):
            maxForCur = 0
            for j in range(cur, len(nums)):
                if nums[j] > nums[cur] and lengths[j] > maxForCur:
                    maxForCur = lengths[j]
            lengths[cur] = maxForCur + 1
        return max(lengths)

# O(n log n) Solution
def lengthOfLIS(nums):
    if len(nums) == 0:
            return 0
        sequence =[]
        for n in nums:
            if not sequence or sequence[-1] < n:
                sequence.append(n)
            else:
                sequence[bisect.bisect_left(sequence, n)] = n
        return len(sequence)

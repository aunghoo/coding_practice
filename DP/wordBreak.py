''' Medium
https://leetcode.com/problems/word-break
'''
# Not optimized yet - only better than 5% of submissions on Leetcode
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        mem = [[-1] * len(s) for i in range(len(s))]
        return self.checkPathExists(s, wordSet, len(s), mem)

    def checkPathExists(self, s, wordSet, col, mem):
        if s[:col] in wordSet:
            return True
        for r in reversed(range(col)):
            if s[r:col] in wordSet:
                if mem[r][col-1] == -1:
                    if self.checkPathExists(s, wordSet, r, mem):
                        return True
                    else:
                        mem[r][col-1] = 0
            mem[r][col-1] = 0
        return False

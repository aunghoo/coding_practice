'''
https://leetcode.com/problems/coin-change
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        mem = {}
        return self.memoizedCoinChange(coins, amount, mem)

    def memoizedCoinChange(self, coins, amount, mem):
        if amount in mem:
            return mem[amount]
        minimum = float('inf')
        for c in coins:
            if c == amount:
                mem[amount] = 1
                return 1
            if c < amount:
                minimum_for_remainder = self.memoizedCoinChange(coins, amount - c, mem)
                if minimum_for_remainder != -1 and minimum_for_remainder < minimum:
                    minimum = minimum_for_remainder
        if minimum != float('inf'):
            mem[amount] = minimum + 1
            return minimum + 1
        mem[amount] = -1
        return -1

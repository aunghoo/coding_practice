import sys
# brute force recursive solution
def coinChangeBruteForce(target, coins):
    if target == 0:
        return 0
    minChange = sys.maxint
    for c in coins:
        if target - c >= 0:
            # optimal change required if we use the current coin
            changeRequired = coinChangeBruteForce(target - c, coins)
            # if optimal change is best, use the current coin
            if changeRequired < minChange:
                minChange = changeRequired
    # counting one for the best coin
    return minChange + 1

print coinChangeBruteForce(13, [1, 5, 7])

'''

test cases:
1, 3, 5, target = 9
1 (optimal remaining num of coins)
3 (optimal)

'''

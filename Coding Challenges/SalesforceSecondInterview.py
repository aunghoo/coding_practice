
#
# Your previous C++ content is preserved below:
#
# Opportunities are deals in progress. Suppose you have an array of Opportunities. Find count of pairs of opportunities, such that sum of the amounts of the opportunities is equal to the given amount
#class Opportunity {
#    int id;
#    int accountId;
#    String name;
#    int amount;
#}
# Typ

import collections


'''
6 3*8
{1:3, 3:5, 5:6, }

target=9
[1,4,5,8,9,8,3,3,6,5,4]

{9:1,3:2,6:1}

2
4
2


8

target =8
[4,4, 3, 4, 1, 4]

{4:4, 3:1, 1:1}
4!/(2*2) = 4*3*2/(2)*2! = 6
3*2/(2*1) = 3

{}
5 [2,3,1,4]
6 [3,3,3,3,3]





O(n) where n = number of opportunities
O(k) where k = number of unique amounts in the opportunities array -> O(n) space complexity
'''
def countOfPairs(opportunities, target):
    seenAmounts = collections.defaultdict(int)
    count = 0
    for o in opportunities:
        seenAmounts[o.amount] += 1
    for s in seenAmounts.keys():
        if target-s in seenAmounts.keys():
        	if target-s == s:
        	    count += (math.factorial(seenAmounts[s]) / 2 * math.factorial(seenAmounts[s]-2))
        	else:
                      count += (seenAmounts[target-s] * seenAmounts[s])
                      seenAmounts.erase(s)
                      seenAmounts.erase(target-s)
    return count

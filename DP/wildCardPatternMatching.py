''' Hard
https://leetcode.com/problems/wildcard-matching
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        cache = [[-1] * (len(p)+1) for i in range(len(s)+1)]
        return True if recursiveMatch(s, p, len(s), len(p), cache) else False

# top down approach
# definition: if there is a way to match first i characters of s with j characters of p, then true, else false
def recursiveMatch(s, p, i, j, cache):
    #base cases
    if i == 0 and j == 0:
        cache[i][j] = 1
        return True
    if j == 0:
        cache[i][j] = 0
        return False
    if i == 0:
        for char in p[:j]:
            if char != '*':
                cache[i][j] = 0
                return False
        cache[i][j] = 1
        return True
    #check if cached
    if cache[i][j] != -1:
        return cache[i][j]
    #conditions
    if (p[j-1] == '*'):
        cache[i][j] = recursiveMatch(s, p, i-1, j, cache) or recursiveMatch(s, p, i, j-1, cache)
    elif (p[j-1] == '?'):
        cache[i][j] = 1 if recursiveMatch(s, p, i-1, j-1, cache) else 0
    else:
        if s[i-1] == p[j-1]:
            cache[i][j] = 1 if recursiveMatch(s, p, i-1, j-1, cache) else 0
        else:
            cache[i][j] = 0
    return cache[i][j]


# bottom up approach
# might still need to elegantly handle base/edge cases
def dpMatch(s, p):
    if len(s) == 0 and len(p) == 0:
        return True
    if len(p) == 0:
        return False
    if len(s) == 0:
        for c in p:
            if c != '*':
                return False
        return True
    table = [[0] * (len(s)) for i in range(len(p))]
    # fill up first row first
    for i in range(len(s)):
        if p[0] == '*':
            table[0][i] = 1
        elif p[0] == '?':
            table[0][i] = 1 if i == 0 else 0
        else:
            table[0][i] = 1 if (i == 0 and p[0]==s[0]) else 0

    allStars = True if p[0] == '*' else False
    # fill up first column
    for j in range(1, len(p)):
        if p[j] == '*':
            table[j][0] = 1 if table[j-1][0] == 1 else 0
        elif p[j] == '?':
            table[j][0] = 1 if allStars else 0
            allStars = False
        else:
            table[j][0] = 1 if (allStars and p[j]==s[0]) else 0
            allStars = False

    # fill up whole table
    if len(p) == 1 or len(s) == 1:
        return True if table[len(p)-1][len(s)-1]==1 else False

    for j in range(1, len(p)):
        for i in range(1, len(s)):
            if p[j]=='*':
                # either we have matched so far, or we can ignore the *
                table[j][i] = 1 if (table[j-1][i]==1 or table[j][i-1]==1) else 0
            elif p[j]=='?':
                table[j][i] = 1 if table[j-1][i-1]==1 else 0
            else:
                table[j][i] = 1 if (table[j-1][i-1]==1 and p[j]==s[i]) else 0

    return True if table[len(p)-1][len(s)-1]==1 else False

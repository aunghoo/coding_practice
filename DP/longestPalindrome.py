'''
https://leetcode.com/problems/longest-palindromic-substring
'''

class Solution(object):
    def longestPalindromeByBottomUpApproach(self, s):
        return botUpPalindrome(s)
    def longestPalindromeByTopDownApproach(self, s):
        cache = [[0] * len(s) for i in range(len(s))]

def botUpPalindrome(s):
    cache = [[0] * len(s) for i in range(len(s))]
    # vary by length of the substring being checked
    for k in range(0, len(s)):
        for i in range(0, len(s) - k):
            j = i + k
            if i == j:
                cache[i][j] = 1
            elif i+1 == j:
                cache[i][j] = 1 if (s[i] == s[j]) else 2
            else:
                if cache[i+1][j-1] == 1 and s[i] == s[j]:
                    cache[i][j] = 1
                else:
                    cache[i][j] = 2

    for length in range(len(s), 0, -1):
        for i in range(0, len(s)):
            j = i + length - 1
            if (j <= len(s) - 1 and cache[i][j] == 1):
                return s[i:j+1]
    return ''

def topDownPalindrome(s, i, j, cache):
    if cache[i][j] != 0:
        return True if cache[i][j] == 1 else False
    if i == j:
        cache[i][j] = 1
        return True
    elif i+1 == j:
        cache[i][j] = 1 if (s[i] == s[j]) else 2
        return True if cache[i][j] == 1 else False
    else:
        if (topDownPalindrome(s, i+1, j-1, cache) and s[i] == s[j]):
            cache[i][j] = 1
            return True
        else:
            cache[i][j] = 2
            return False

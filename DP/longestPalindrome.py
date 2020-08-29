'''
https://leetcode.com/problems/longest-palindromic-substring
'''

class Solution:
    '''
    Test cases:
    ""
    "a"
    "abcdefg"
    "abcba"
    "abba"
    "aibcb"
    "aaaaaaaaaaaaaaaaaaaaaaaaacaaaaaaaaaaaaaaaaaaa"
    '''

    def longestPalindrome(self, s: str) -> str:
        return self.dpPalindrome(s)
        # return self.memoPalindrome(s) # This is the solution with topdown memoization

    def memoPalindrome(self, s):
        table = [[-1] * len(s) for i in range(len(s))]
        # Go through various lengths from largest to smallest
        for length in range(len(s), 0, -1):
            l = 0
            while l+length <= len(s):
                if self.isPalindrome(s, l, l+length-1, table):
                    return s[l:l+length]
                l += 1
        return ''

    def isPalindrome(self, s, l, r, table):
        if l == r:
            table[l][r] = True
            return True
        if l+1 == r:
            table[l][r] = s[l] == s[r]
            return table[l][r]
        if table[l][r] != -1:
            return table[l][r]
        if s[l] == s[r]:
            table[l][r] = self.isPalindrome(s, l+1, r-1, table)
            return table[l][r]

    def dpPalindrome(self, s):
        table = [[-1] * len(s) for i in range(len(s))]
        longest = ''
        # Iterate through the table based on lengths
        # Start with length 1 words, then 2, etc
        for length in range(len(s)):
            for l in range(len(s)):
                r = l + length
                if r >= len(s):
                    continue
                if l == r:
                    table[l][r] = 1
                elif l+1 == r:
                    table[l][r] = 1 if s[l] == s[r] else 0
                elif s[l] == s[r] and table[l+1][r-1] == 1:
                    table[l][r] = 1
                else:
                    table[l][r] = 0
                if table[l][r] == 1:
                    longest = s[l:r+1]
        return longest

    ''' 
    Next two functions use Center method
    
    '''
    def getPalindromesFromCenter(self, s):
        longest = ''
        for i in range(len(s)):
            # Get character at i to be center
            palindrome = self.getLongestPalindromeFromCenter(i, s, False)
            if len(palindrome) > len(longest):
                longest = palindrome
            # Check with both character at i and i + 1 to be center (halfway case)
            if i != len(s) - 1:
                palindrome = self.getLongestPalindromeFromCenter(i, s, True)
                if len(palindrome) > len(longest):
                    longest = palindrome
        return longest

    def getLongestPalindromeFromCenter(self, i, s, halfway):
        l, r = i, i
        longest = ''
        if halfway:
            r = i + 1
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                return longest
            longest = s[l:r+1]
            l -= 1
            r += 1
        return longest
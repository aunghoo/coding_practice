''' Medium
https://leetcode.com/problems/decode-ways/
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        num_ways_back, num_ways_here = 1, 1
        for i in range(1,len(s)):
            cur = 0
            if int(s[i]) > 0:
                cur += num_ways_here
            if i >0 and int(s[i-1])>0:
                two_letter = int(s[i-1:i+1])
                if two_letter > 0 and two_letter <= 26:
                    cur += num_ways_back
            num_ways_back = num_ways_here
            num_ways_here = cur

        return num_ways_here

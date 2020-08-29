''' Easy
https://leetcode.com/problems/valid-parentheses/
'''

from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = deque()
        for c in s:
            if (c=='(' or c=='{' or c=='['):
                q.append(c)
            else:
                if not q:
                    return False
                openBracket = q.pop()
                if not matching(openBracket, c):
                    return False
        return True if not q else False

def matching(o, c):
    if o=='(' and c==')':
        return True
    if o=='[' and c==']':
        return True
    if o=='{' and c=='}':
        return True
    return False

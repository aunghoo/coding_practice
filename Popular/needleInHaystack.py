''' Easy
https://leetcode.com/problems/implement-strstr
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        solution = 0
        found = False
        if needle == '':
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                index = i
                match = True
                if len(haystack) - i < len(needle):
                    break
                for n in needle:
                    if index >= len(haystack) or haystack[index] != n:
                        match = False
                        break
                    index += 1
                if match:
                    solution = i
                    found = True
                    break
        return solution if found else -1

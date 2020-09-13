class Solution:
    def isValid(self, s: str) -> bool:
        deq = deque()
        bracketMap = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in {'(', '{', '['}:
                deq.append(char)
            else:
                if not deq:
                    return False
                closeBracket = deq.pop()
                if char != bracketMap[closeBracket]:
                    return False
        if deq:
            return False
        return True
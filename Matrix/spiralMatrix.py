''' Medium
https://leetcode.com/problems/spiral-matrix/
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiralOrderArr = []

        rstart = 0
        cstart = 0
        rend = len(matrix)-1
        cend = len(matrix[0])-1 if matrix else 0

        while (cend >= cstart and rend >= rstart):
            if cstart == cend:
                for r in range(rstart, rend+1):
                    spiralOrderArr.append(matrix[r][cstart])
                break
            if rstart == rend:
                for c in range(cstart, cend+1):
                    spiralOrderArr.append(matrix[rstart][c])
                break
            for c in range(cstart, cend):
                spiralOrderArr.append(matrix[rstart][c])
            for r in range(rstart, rend):
                spiralOrderArr.append(matrix[r][cend])
            for c in range(cend, cstart, -1):
                spiralOrderArr.append(matrix[rend][c])
            for r in range(rend, rstart, -1):
                spiralOrderArr.append(matrix[r][cstart])
            rstart += 1
            rend -= 1
            cstart += 1
            cend -= 1

        return spiralOrderArr
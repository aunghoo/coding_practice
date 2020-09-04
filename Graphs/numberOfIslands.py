''' Medium
https://leetcode.com/problems/number-of-islands/
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])

        def visit(r, c, grid):
            grid[r][c] = "0"
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if nr >= 0 and nc >= 0 and nr < R and nc < C:
                    if grid[nr][nc] == "1":
                        visit(nr, nc, grid)
            return True
    
        num = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    num += 1
                    visit(r, c, grid)
        return num
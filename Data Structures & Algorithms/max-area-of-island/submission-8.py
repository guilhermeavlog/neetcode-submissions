class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        area = 0

        def dfs_recursive(x, y):
            nonlocal area
            neighbors = [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]

            for nx, ny in neighbors:
                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                    if grid[nx][ny] != 0:
                        area += 1
                        grid[nx][ny] = 0
                        dfs_recursive(nx, ny)

        rows, columns = len(grid), len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] != 0:
                    area = 1
                    grid[r][c] = 0
                    dfs_recursive(r, c)
                    max_area = max(area, max_area)

        return max_area

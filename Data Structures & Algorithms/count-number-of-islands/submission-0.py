class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x, y):
            if grid[x][y] == '0':
                return 
            
            grid[x][y] = '0'

            directions = [[0,1],[1,0],[-1,0],[0,-1]]

            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]
                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                    dfs(nx,ny)
        
        rows, columns = len(grid), len(grid[0])
        island_count = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)

        return island_count


                
        
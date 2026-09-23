class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
 
        we can either go down or right at start
        so total paths to down and right is 1
        whenever there is a choice between down or right we add 1 to path 
        we need to add to whatever is in the grid position we are going to 

        each grid position rerpesents numbers of ways to get to positon

        '''
        grid = [ [0] * n for _ in range(m) ]

        for i in range(m):
            grid[i][0] = 1
        
        for j in range(n):
            grid[0][j] = 1
        

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[-1][-1] 




        
        
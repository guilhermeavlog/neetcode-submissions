class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False

        def dfs(coord, visited, i):
            nonlocal found 

            x, y = coord

            if found:
                return

            if coord in visited:
                return 

            if board[x][y] != word[i]:
                return 

            if i == len(word) - 1:
                found = True
                return 


            visited.add(coord)
            i += 1

            new_coord = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

            for nx, ny in new_coord:
                if (nx, ny) not in visited:
                    if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]):
                        dfs((nx,ny), visited, i)
            visited.remove(coord)

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs((i,j), set(), 0)

                if found:
                    return True
            

        return False
            

            

            

        
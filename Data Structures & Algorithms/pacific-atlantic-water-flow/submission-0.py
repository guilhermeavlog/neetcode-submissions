class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, columns = len(heights), len(heights[0])

        self.pacific, self.atlantic = False, False

        def dfs(node, visited):
            if node in visited:
                return
            
            if node[0] == 0 or node[1] == 0:
                self.pacific = True
            
            if node[0] == rows - 1 or node[1] == columns - 1:
                self.atlantic = True 

            visited.add(node)

            neighbors = [(node[0], node[1]+1), (node[0]+1, node[1]), (node[0], node[1] - 1), (node[0] - 1, node[1])]

            for neighbor in neighbors:  
                if neighbor not in visited:
                    if neighbor[0] < rows and neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[1] < columns:
                        if heights[neighbor[0]][neighbor[1]] <= heights[node[0]][node[1]]:    
                            dfs(neighbor, visited)

        ans = []

        for r in range(rows):
            for c in range(columns):
                self.pacific, self.atlantic = False, False
                dfs((r,c), set())

                if self.pacific and self.atlantic:
                    ans.append((r,c))

        return ans



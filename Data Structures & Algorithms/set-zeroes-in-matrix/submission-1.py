class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows, columns = len(matrix), len(matrix[0])
        zero_pos = set()

        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    zero_pos.add((r,c))

        for r,c in zero_pos:
            for i in range(columns):
                matrix[r][i] = 0
            for j in range(rows):
                matrix[j][c] = 0

                
      
       
                


        
        
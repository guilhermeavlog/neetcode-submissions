class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows, columns = len(matrix), len(matrix[0])
        zero_rows, zero_columns = set(), set()
        
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    zero_rows.add(r) 
                    zero_columns.add(c)

        for row in zero_rows:
            for c in range(columns):
                matrix[row][c] = 0

        for col in zero_columns:
            for r in range(rows):
                matrix[r][col] = 0

                
      
       
                


        
        
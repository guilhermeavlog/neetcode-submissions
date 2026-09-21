class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        use first row and first column to say is there a 0 here 
        mark as 0 if yes
        
        make sure to mark if there is 0 in first row and column so we dont lose that information.
        '''

        rows, columns = len(matrix), len(matrix[0])
        first_column_zero, first_row_zero = False, False
        
        for r in range(rows):
            if matrix[r][0] == 0:
                first_column_zero = True

        for c in range(columns):
            if matrix[0][c] == 0:
                first_row_zero = True
            
        for r in range(1, rows):
            for c in range(1, columns):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, columns):
                    matrix[r][c] = 0
        
        for c in range(1, columns):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
            
        if first_row_zero:
            for c in range(columns):
                matrix[0][c] = 0
        if first_column_zero:
            for r in range(rows):
                matrix[r][0] = 0

                

        
    

                
      
       
                


        
        
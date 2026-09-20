class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        first transpose:
        keep diagonal same 
        just flip xy to yx and yx to xy 

        then we need to flip based on horizontal center line
        we could use two pointers
        one starts at beginning other one at end of array do that for every row 

        '''

        n = len(matrix)

        for r in range(n):
            for c in range(r+1, n):
                if r == c: continue 

                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp
        
        for row in range(n):
            l, r = 0, n - 1

            while l <= r:
                tmp = matrix[row][l]
                matrix[row][l] = matrix[row][r]
                matrix[row][r] = tmp
                l += 1
                r -= 1
        



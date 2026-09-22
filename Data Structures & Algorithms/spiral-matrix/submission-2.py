class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        m, n = len(matrix), len(matrix[0])
        direction = RIGHT
        ans = []

        right_bound, left_bound, upper_bound, lower_bound = n, 0, 0, m
        r, c = 0, 0

        while (m * n) > len(ans):
            if direction == RIGHT:
                for i in range(left_bound, right_bound):
                    ans.append(matrix[r][i])
                direction = DOWN
                upper_bound += 1
                c = right_bound - 1
                r += 1
            
            elif direction == DOWN:
                for i in range(upper_bound, lower_bound):
                    ans.append(matrix[i][c])
                direction = LEFT
                right_bound -= 1
                r = lower_bound - 1
            
            elif direction == LEFT:
                for i in range(right_bound - 1, left_bound - 1, -1):
                    ans.append(matrix[r][i])
                direction = UP 
                lower_bound -= 1
                c = left_bound 

            elif direction == UP:
                for i in range(lower_bound - 1, upper_bound - 1, -1):
                    ans.append(matrix[i][c])
                direction = RIGHT
                left_bound += 1
                r = upper_bound 
                
        return ans 
            
                



            

            
                
        
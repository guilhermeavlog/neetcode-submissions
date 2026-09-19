class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        if we have 1101
        ans should be 1011 
        we can apply 1 mask with and to get single right most bit 
        we need to make space for new right most digit first by shifting left
        and then store in res using or with bit 
        afterwards we discard rightmost bit by shifting right 

        ''' 

        ans = 0
        for _ in range(32):
            ans = ans << 1
            bit = n & 1
            ans = ans | bit
            n = n >> 1

        return ans 

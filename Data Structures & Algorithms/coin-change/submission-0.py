class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ''' 
        first we need to make each amount 

        to make 0 it takes 0 coins

        to make 1 we can either 
        
        '''

        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0


        for i in range(amount+1):
            for c in range(n):
                if coins[c] <= i:
                    dp[i] = min(dp[i], dp[i - coins[c]] + 1)

        if dp[-1] == float('inf'): return -1
        else: return dp[-1]



        
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        actions: rob house i or rob house i + 1
        if rob house i, rob house i + 2 or rob house i + 3
        if rob house i + 1 rob house i + 3 or i + 4

        at i = 0
        we have max amount we get from robbing so far
        which is just nums[0], at house 1 we have max of nums[0] and nums[1] 
        those are BASE CASES.

        we can get nums[2] by getting max between robbing house 0 and 2 vs just 1.
        TRANSITIONS FIGURED OUT TOO.

        DEAL WITH  FIRST AND LAST HOUSE BEING CONNECTED BY RUNNING ON SLICED STRING NUMS[:LEN(NUMS)-1]]
        AND ALSO ON NUMS[1:]
        ''' 
        

        def max_amount_robbed(arr):
            n = len(arr)

            if not arr:
                return 0 
            if n < 2:
                return arr[0]
            
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2]+arr[i])
            
            return dp[-1]

        size = len(nums)

        if size < 2:
            return nums[0]
            
        return max(max_amount_robbed(nums[:size-1]), max_amount_robbed(nums[1:]))




        
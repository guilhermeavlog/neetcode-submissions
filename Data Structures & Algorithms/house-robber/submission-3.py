class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        we either rob house i or dont 
        - if robbed: we either rob house i+2 or dont 
        - if not robbed we either rob house i+1 or dont

        take max between robbing house 1 or not 
        '''
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return nums[0]
        if len(nums) < 3:
            return max(nums[0], nums[1])

        n = len(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[-1]
            




        
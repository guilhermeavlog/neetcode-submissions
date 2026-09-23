class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        we start at i = 0
        longest subsequence is just 1 there 
        
        at i = 1 
        longest subsequence depends on i - 1
        if i - 1 value is less length is 2 else its 1

        at i = 2 
        longest subsequence is either:
        dp[i-1] + 1 if nums[i] > nums[i-1]
        or dp[i - 1] otherwise

        '''
        if not nums:
            return 0

        dp = [1] * len(nums)
       
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
        
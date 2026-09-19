class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n * (n+1) // 2

        for i in range(len(nums)):
            ans -= nums[i]

        return ans
        
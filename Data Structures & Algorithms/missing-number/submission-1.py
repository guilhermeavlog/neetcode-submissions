class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)+1):
            if i < len(nums):
                ans = ans ^ i ^ nums[i]
            else:
                ans = ans ^ i


        return ans
        
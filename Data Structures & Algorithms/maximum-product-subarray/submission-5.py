class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = min_p = global_max = nums[0]
        
        for i in range(1, len(nums)):
            tmp = min_p
            min_p = min(nums[i], nums[i]*min_p, nums[i]*max_p)
            max_p = max(nums[i], nums[i]*tmp, nums[i]*max_p)
            global_max = max(global_max, max_p)

        return global_max

        
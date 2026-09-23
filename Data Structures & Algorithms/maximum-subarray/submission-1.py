class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Kadane's algorithm

        we start fresh if adding new element would reduce the curr_sum
        else we just add element to curr_sum

        then compute max_sum

        '''

        curr_sum, max_sum = nums[0], nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])

            max_sum = max(max_sum, curr_sum)

        return max_sum 

        
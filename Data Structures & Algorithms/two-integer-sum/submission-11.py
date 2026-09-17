class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i in range(len(nums)):
            second_val = target - nums[i]

            if second_val in seen:
                return [seen[second_val], i]

            seen[nums[i]] = i

        return []
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}   

        for i in range(len(nums)):
            first_val = target - nums[i]
        
            if first_val in hashMap:
                return [hashMap[first_val], i]

            hashMap[nums[i]] = i

        return [hashMap[first_val], i]






        
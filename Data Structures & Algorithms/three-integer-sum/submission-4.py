class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        solution = []

        for pivot in range(len(nums)):
            if pivot > 0 and nums[pivot] == nums[pivot-1]:
                continue
            left = pivot + 1
            right = len(nums) - 1

            

            while left < right:
                summation = nums[pivot] + nums[left] + nums[right]
                
                if summation == 0:
                    solution.append([nums[pivot], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while not left == pivot+1 and left < right and nums[left] == nums[left-1]:
                        left += 1
                    while not right == len(nums)-1 and left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif summation < 0:
                    left += 1
                elif summation > 0:
                    right -= 1

        return solution

            



                
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_val = 1
        left_mult = [1]
        for i in range(len(nums)): #everything on left side []
            left_mult.append(left_val*nums[i])
            left_val *= nums[i]

        right_val = 1
        right_mult = [1]
        for j in range(len(nums)-1, -1, -1): #everything on right side []
            right_mult.append(right_val*nums[j])
            right_val *= nums[j]

        solution = []
        for g in range(len(nums)): # multiply both sides
            length = len(nums) - 1
            solution.append(left_mult[g] * right_mult[length-g])

        return solution
            

        


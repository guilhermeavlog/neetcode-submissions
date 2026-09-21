class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for i in range(len(nums)):
            if max_jump < 0:
                return False 
                
            max_jump = max(max_jump, nums[i])
            max_jump -= 1
            
        
        return True 
        

        

           

    


        

        
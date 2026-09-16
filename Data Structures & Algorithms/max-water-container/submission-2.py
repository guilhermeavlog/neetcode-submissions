class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        best_area = 0
        right = len(heights) - 1

        while left < right:
            length = right - left
            new_area = min(heights[left], heights[right]) * length

            if new_area > best_area:
                best_area = new_area
            
            if heights[right] < heights[left]:
                right -= 1 

            else:
                left += 1 

        return best_area
            

                

        
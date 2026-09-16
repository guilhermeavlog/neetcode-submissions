class Solution:
    def trap(self, height: List[int]) -> int:
        right_max, left_max = [0] * len(height), [0] * len(height)
        right_max[-1], left_max[0] = height[-1], height[0]

        for l in range(1, len(height)):
            left_max[l] = (max(height[l], left_max[l-1]))

        for r in range(len(height) - 2, -1, -1):
            right_max[r] = (max(height[r], right_max[r+1]))
        
        water_sum = 0

        for h in range(len(height)):
            water_sum += min(right_max[h], left_max[h]) - height[h]

        return water_sum
    




        
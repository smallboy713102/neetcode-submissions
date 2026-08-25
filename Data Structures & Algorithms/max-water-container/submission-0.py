class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxWater = -1
        while l < r:
            maxWater = max(maxWater,min(heights[l],heights[r])*(r-l))
            if heights[l] < heights[r] : l+=1
            else: r -=1;
        return maxWater
class Solution(object):
    def maxArea(self, height):
        n = len(height)
        l_point = 0
        r_point = n - 1
        maxWater = 0
        while l_point < r_point:
            if height[l_point] <= height[r_point]:
                water = (r_point - l_point) * height[l_point]
                l_point += 1
            else:
                water = (r_point - l_point) * height[r_point]
                r_point -= 1
            maxWater = max(maxWater, water)
        return maxWater

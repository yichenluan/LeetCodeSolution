class Solution(object):
    def trap(self, height):
        n = len(height)
        left = 0
        right = n - 1
        res = 0
        maxLeft = maxRight = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        return res

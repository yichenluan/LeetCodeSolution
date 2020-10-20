class Solution(object):
    def missingNumber(self, nums):
        ans = len(nums)
        for i, num in enumerate(nums):
            ans ^= i
            ans ^= num
        return ans

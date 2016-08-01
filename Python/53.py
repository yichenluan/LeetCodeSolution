class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0
        currSum = maxSum = nums[0]
        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)
        return maxSum


class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0
        return self.d_c_handler(nums)

    def d_c_handler(self,nums):
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) / 2
        left = nums[:mid]
        right = nums[mid:]
        leftMax = self.d_c_handler(left)
        rightMax = self.d_c_handler(right)
        lMax = -99999999
        rMax = -99999999
        l_sum = r_sum = 0
        for i in left[::-1]:
            l_sum += i
            lMax = max(lMax, l_sum)
        for i in right:
            r_sum += i
            rMax = max(rMax, r_sum)
        crossMax = lMax + rMax
        return max(crossMax, leftMax, rightMax)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    case = Solution()
    print case.maxSubArray(nums)


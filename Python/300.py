'''LIS

Binary Search Solution:
https://discuss.leetcode.com/topic/46913/o-nlogn-clean-and-easy-java-dp-binary-search-solution-with-detailed-explanation
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            print dp
        return max(dp)


if __name__ == '__main__':
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    case = Solution()
    print case.lengthOfLIS(nums)

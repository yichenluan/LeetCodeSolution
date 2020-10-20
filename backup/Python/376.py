class Solution(object):
    def wiggleMaxLength(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        res = 2
        i = 1
        while i < len(nums) - 1:
            if nums[i] > nums[i - 1]:
                for j in range(i, len(nums)):
                    if nums[j] < nums[j -1]:
                        res += 1
                        break
            else:
                for j in range(i, len(nums)):
                    if nums[j] > nums[j - 1]:
                        res += 1
                        break
            i = j
        if res == 2 and nums[0] == nums[-1]:
            res = 1
        return res


if __name__ == '__main__':
    # nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    nums = [1, 7, 4, 9, 2, 5]
    case = Solution()
    print case.wiggleMaxLength(nums)

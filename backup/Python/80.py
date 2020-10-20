class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        count = 0
        flag = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                flag += 1
                if flag > 1:
                    count += 1
            if nums[i] != nums[i - 1]:
                flag = 0
            if flag <= 1:
                nums[i - count] = nums[i]
        return n - count


if __name__ == '__main__':
    nums = [1,1,1,1,3,3]
    case = Solution()
    print case.removeDuplicates(nums)

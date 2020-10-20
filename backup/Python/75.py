class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        i = 0
        while l < r and i < r+1:
            while nums[i] == 2 and i < r+1:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            i += 1
        print nums
        

if __name__ == '__main__':
    nums = [0,1,2,2,1,0,1,2,0]
    case = Solution()
    case.sortColors(nums)

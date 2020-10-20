class Solution(object):
    def minSubArrayLen(self, s, nums):
        left = right = mini_length = 0
        curr_sum = nums[0] if nums else 0
        
        while right < len(nums):

            while curr_sum < s:
                right += 1
                if right == len(nums):
                    return mini_length
                curr_sum += nums[right]

            if (right - left + 1) < mini_length or not mini_length:
                mini_length = right - left + 1

            curr_sum -= nums[left]
            left += 1
        return mini_length

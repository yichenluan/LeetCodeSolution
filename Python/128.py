class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}
        maxLength = 1
        for n in nums:
            length = 1
            left = 0
            right = 0
            if n in dictionary:
                continue
            dictionary[n] = 1
            if n - 1 in dictionary:
                length += dictionary[n - 1]
                left = dictionary[n - 1]
            if n + 1 in dictionary:
                length += dictionary[n + 1]
                right = dictionary[n + 1]
            dictionary[n - left] = length
            dictionary[n + right] = length
            if maxLength < length:
                maxLength = length
        return maxLength

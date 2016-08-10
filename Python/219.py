class Solution(object):
    def containNearbyDuplicate(self, nums, k):
        hash_map = dict()
        for i in range(len(nums)):
            if nums[i] in hash_map:
                value = hash_map[nums[i]]
                if i - value <= k:
                    return True
                else:
                    hash_map[nums[i]] = i
            else:
                hash_map[nums[i]] = i
        return False

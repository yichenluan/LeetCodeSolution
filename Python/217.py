class Solution(object):
    def containsDuplicate(self, nums):
        hash_table = dict()
        for num in nums:
            val = hash_table.get(num, 0) + 1
            if val > 1:
                return True
            else:
                hash_table[num] = val
        return False

class Solution(object):
    def intersect(self, nums1, nums2):
        nums1_hash = dict()
        for n in nums1:
            nums1_hash[n] = nums1_hash.get(n, 0) + 1
        res = list()
        for n in nums2:
            count = nums1_hash.get(n, 0)
            if count > 0:
                res.append(n)
                nums1_hash[n] = count - 1
        return res

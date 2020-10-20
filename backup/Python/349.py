class Solution(object):
    def intersection(self, nums1, nums2):
        res_dict = dict()
        for num in nums1:
            res_dict[num] = [1,0]
        for num in nums2:
            temp = res_dict.get(num, [0, 0])
            temp[1] = 1
            res_dict[num] = temp
        res_list = list()
        for key, value in res_dict.iteritems():
            if value == [1, 1]:
                res_list.append(key)
        return res_list

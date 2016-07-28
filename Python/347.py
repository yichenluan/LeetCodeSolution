class Solution(object):
    def topKFrequent(self, nums, k):
        hash_dict = dict()
        lst = list()
        for num in nums:
            hash_dict[num] = hash_dict.get(num, 0) + 1
        for key,val in hash_dict.iteritems():
            lst.append((val, key))
        lst.sort(reverse=True)
        res = list()
        for i in range(k):
            res.append(lst[i][1])
        return res

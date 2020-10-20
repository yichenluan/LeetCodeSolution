class Solution(object):
    def majorityElement(self, nums):
        key = len(nums) / 3
        hashDict = dict()
        res = list()
        for num in nums:
            count = hashDict.get(num) + 1
            hashDict[num] = count
            if count > key and num not in res:
                res.append(num)
        return res


'''
Boyer-Moore Majority Vote algorithm
https://segmentfault.com/a/1190000004905350
'''
class Solution(object):
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, 1
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            count1 -= 1
            count2 -= 1

    return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):

        def handler(nums1, nums2):
            n1 = len(nums1)
            if n1 == 0:
                return []
            if n1 == 1:
                return [[nums1[0], num] for num in nums2]
            mid = n1 / 2
            left = handler(nums1[:mid], nums2)
            right = handler(nums1[mid:], nums2)
            res = merge(left, right)
            return res

        def merge(left, right):
            res = list()
            n_left = len(left)
            n_right = len(right)
            i = j = 0
            res_l = 0
            while i < n_left and j < n_right:
                if sum(left[i]) < sum(right[j]):
                    res.append(left[i])
                    res_l += 1
                    i += 1
                else:
                    res.append(right[j])
                    res_l += 1
                    j += 1
                if res_l > k:
                    return res
            res += left[i:]
            res += right[j:]
            return res

        return handler(nums1, nums2)[:k]


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 10
    case = Solution()
    print case.kSmallestPairs(nums1, nums2, k)

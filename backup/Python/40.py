class Solution(object):
    def combinationSum2(self, candidates, target):
        res = list()

        def handler(candidates, target, curr):
            if target == 0:
                res.append(curr)
                return
            pre = None
            for i in range(len(candidates)):
                if candidates[i] > target:
                    continue
                if candidates[i] == pre:
                    continue
                pre = candidates[i]
                handler(candidates[i+1:], target-candidates[i], curr+[candidates[i]])
        candidates.sort()
        handler(candidates, target, [])
        return res

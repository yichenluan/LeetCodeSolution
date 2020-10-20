class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        coure_array = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        res = []
        for edge in prerequisites:
            coure_array[edge[0]].append(edge[1])

        i = 0
        while i < numCourses:
            if len(coure_array[i]) == 0:
                res += i,
                visit[i] = -1
            i += 1
        def dfs(x, res):
            if visit[x] == -1:
                return False
            if visit[x] == 1:
                return True

            visit[x] = 1
            for v in coure_array[x]:
                if dfs(v, res):
                    return True
            visit[x] = -1
            res.append(x)
            return False

        for i in xrange(numCourses):
            if dfs(i, res):
                return []
        return res

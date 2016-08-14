class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        stack = list()
        res = list()
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
            indegree[pair[1]] = indegree[pair[1]] + 1
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
        while stack:
            node = stack.pop()
            res.append(node)
            for num in graph[node]:
                indegree[num] -= 1
                if indegree[num] == 0:
                    stack.append(num)
        return len(res) == numCourses

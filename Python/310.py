class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n <= 1:
            return [0]
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        leaves = [i for i in xrange(n) if len(graph[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = list()
            for i in leaves:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves

class Solution(object):
    def cloneGraph(self, start):
        if not start: return None
        new, old, queue = {}, {}, [start]
        for node in queue:
            if node.label in new: continue
            new[node.label] = UndirectedGraphNode(node.label)
            old[node.label] = node
            for neigh in node.neighbors: queue += neigh,
        for label in new:
            for neighl in old[label].neighbors:
                new[label].neighbors += new[neighl.label],
        return new.pop(start.label, None)

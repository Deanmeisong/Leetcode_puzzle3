class Solution:
    def deleteTreeNodes(self, nodes, parent, value):
        def dfs(i):
            s, m = value[i], 1
            for j in g[i]:
                t, n = dfs(j)
                s += t
                m += n
            if s == 0:
                m = 0
            return (s, m)

        from collections import defaultdict
        g = defaultdict(list)
        for i in range(1, nodes):
            g[parent[i]].append(i)
        return dfs(0)[1]

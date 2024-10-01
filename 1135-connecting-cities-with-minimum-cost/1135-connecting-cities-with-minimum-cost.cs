public class Solution {
    public int MinimumCost(int n, int[][] connections) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++)
        {
            parent[i] = i;
        }

        Array.Sort(connections, (a, b) => a[2].CompareTo(b[2]));

        Func<int, int> find = null;
        find = x =>
        {
            if (x != parent[x])
            {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        };

        int totalCost = 0;
        foreach (var connection in connections)
        {
            int x = connection[0] - 1, y = connection[1] - 1, cost = connection[2];
            if (find(x) == find(y)) continue;

            parent[find(x)] = find(y);
            totalCost += cost;

            if (--n == 1)
            {
                return totalCost;
            }
        }

        return -1;
    }
}
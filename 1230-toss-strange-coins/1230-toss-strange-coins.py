class Solution(object):
    def probabilityOfHeads(self, prob, target):
        n = len(prob)
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, p in enumerate(prob, 1):
            for j in range(min(i, target)+1):
                f[i][j] = f[i-1][j]*(1-p)
                if j:
                    f[i][j] += p * f[i - 1][j - 1]
        return f[n][target]
        
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        def dfs(cnt):
            ans = 0
            for i, x in cnt.items():
                if x > 0:
                    ans += 1
                    cnt[i] -= 1
                    ans += dfs(cnt)
                    cnt[i] += 1
            return ans

        cnt = Counter(tiles)
        return dfs(cnt)
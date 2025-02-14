/**
 * @param {string} tiles
 * @return {number}
 */
var numTilePossibilities = function(tiles) {
    const cnt = new Array(26).fill(0);
    for (const c of tiles) {
        ++cnt[c.charCodeAt(0) - 'A'.charCodeAt(0)];
    }

    const dfs = (cnt) => {
        let res = 0;
        for (let i = 0; i < 26; ++i) {
            if (cnt[i] > 0) {
                ++res;
                --cnt[i];
                res += dfs(cnt);
                ++cnt[i];
            }
        }
        return res;
    };

    return dfs(cnt);
};
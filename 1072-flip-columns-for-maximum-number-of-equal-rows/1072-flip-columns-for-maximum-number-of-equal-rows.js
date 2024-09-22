/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxEqualRowsAfterFlips = function(matrix) {
    let cnt = new Map();
    let ans = 0;

    for (let row of matrix) {
        let s = "";
        for (let x of row) {
            s += (row[0] === 0 ? x : (x ^ 1));  // Flip the bits based on the first element of the row
        }
        cnt.set(s, (cnt.get(s) || 0) + 1);  // Increment the count for the string pattern
        ans = Math.max(ans, cnt.get(s));  // Keep track of the maximum count
    }

    return ans;
};
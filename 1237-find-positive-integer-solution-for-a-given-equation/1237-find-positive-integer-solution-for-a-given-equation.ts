/**
 * // This is the CustomFunction's API interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *      f(x: number, y: number): number {}
 * }
 */

function findSolution(customfunction: CustomFunction, z: number): number[][] {
	const ans: number[][] = [];
    for (let x = 1; x <= 1000; x++) {
        let l = 1, r = 1000;
        while (l < r) {
            let m = Math.floor((r - l) / 2) + l;
            if (customfunction.f(x, m) >= z) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        if (customfunction.f(x, l) === z) {
            ans.push([x, l]);
        }
    }
    return ans;
};
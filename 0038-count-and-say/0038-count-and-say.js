/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    let res = "1";
    for (let i = 1; i < n; i++) {
        res = buildNext(res);
    }
    return res;
};

function buildNext(s) {
    let result = "";
    let count = 1;
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i - 1]) {
            count++;
        } else {
            result += count + s[i - 1];
            count = 1;
        }
    }
    result += count + s[s.length - 1];
    return result;
}
const fs = require('fs');
const input = fs
    .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .trim()
    .split(" ")
    .map(Number);
const k = input[0];
const n = input[1];
const m = input[2];
let ans = k * n - m;
if (ans > 0)
    console.log(ans);
else
    console.log(0);
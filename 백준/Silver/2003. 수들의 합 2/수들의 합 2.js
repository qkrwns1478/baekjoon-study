const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = [];
let lineCount = 0;

rl.on('line', function (line) {
    input.push(line);
    lineCount++;
}).on('close', function () {
    const [n, m] = input[0].split(' ').map(Number);
    const A = input[1].split(' ').map(Number);
    
    let i = 0;
    let j = 0;
    let cnt = 0;
    while (j < n) {
        let sumA = 0;
        for (let k = i; k <= j; k++) {
            sumA += A[k];
        }
        if (sumA === m) {
            cnt++;
            j++;
        } else if (sumA < m) {
            j++;
        } else {
            i++;
        }
    }
    console.log(cnt);
});
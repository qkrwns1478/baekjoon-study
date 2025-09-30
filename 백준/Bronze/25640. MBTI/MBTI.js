const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let lineCount = 0;

rl.on('line', function(line) {
    input.push(line);
    lineCount++;
}).on('close', function() {
    let lineIndex = 0;
    const s = input[lineIndex++];
    const n = Number(input[lineIndex++]);

    let cnt = 0;
    for (let i = 0; i < n; i++) {
        const t = input[lineIndex++];
        if (s === t) {
            cnt += 1;
        }
    }

    console.log(cnt);
});
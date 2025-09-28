const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let t, arr;
rl.on('line', function (line) {
    const input = line.split(' ');
    if (t === undefined) {
        t = input[0];
    } else {
        arr = input;
    }
}).on('close', function () {
    const answer = arr.filter(i => i === t).length;
    console.log(answer);
});
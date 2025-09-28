const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let x, y, z, u, v, w;
let lineCount = 0;
rl.on('line', function (line) {
    lineCount++;
    const inputs = line.split(' '); 
    if (lineCount === 1) {
        [x, y, z] = inputs;
    } else if (lineCount === 2) {
        [u, v, w] = inputs;
    }
}).on('close', function () {
    const a = x * (u / 100);
    const b = y * (v / 50);
    const c = z * (w / 20);
    console.log(a + b + c);
});
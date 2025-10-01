const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputs = [];
let count = 0;

rl.on('line', (line) => {
    inputs.push(Number(line));
    count++;
}).on('close', () => {
    let n = 0;
    for (let i = 0; i < 4; i++) {
        n += inputs[i];
    }
    console.log(Math.floor(n / 60));
    console.log(n % 60);
});
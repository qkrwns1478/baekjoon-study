const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

inputs = [];
lineIndex = 0;

rl.on('line', (line) => {
    inputs.push(line);
}).on('close', () => {
    const money = [25, 10, 5, 1];
    const t = parseInt(inputs[lineIndex++]);
    for (let i = 0; i < t; i++) {
        let c = parseInt(inputs[lineIndex++]);
        const res = [];

        for (const m of money) {
            res.push(Math.floor(c / m));
            c = c % m;
        }
        console.log(res.join(' '));
    }
});
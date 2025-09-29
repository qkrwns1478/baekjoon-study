const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    const d = Number(input[0]);
    const gcd = (a, b) => a % b == 0 ? b : gcd(b, a % b);
    const g = gcd(d, 360);
    console.log(360 / g);
});
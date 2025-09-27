const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    let n = Number(line);
    let oe = "odd";
    if (n % 2 == 0)
        oe = "even";
    console.log(n + " is " + oe);
});
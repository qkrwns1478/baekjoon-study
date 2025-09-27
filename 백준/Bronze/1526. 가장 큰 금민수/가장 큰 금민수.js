const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function isEqual(setA, setB) {
    if (setA.size !== setB.size) {
        return false;
    }
    for (let item of setA) {
        if (!setB.has(item)) {
            return false;
        }
    }
    return true;
}

rl.on('line', function (line) {
    input = line.split(' ');
    const n = input[0];
    const kms = [new Set(['4']), new Set(['7']), new Set(['4', '7'])];

    for (let i = n; i > 3; i--) {
        const x = new Set(String(i).split(''));
        let flag = false;
        for (let target of kms) {
            if (isEqual(x, target)) {
                console.log(i);
                flag = true;
                break;
            }
        }
        if (flag)
            break;
    }
});
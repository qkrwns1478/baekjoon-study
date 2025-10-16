const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    input = line.split(' ');
}).on('close', () => {
    const x = Number(input[0])
    const y = Number(input[1])
    
    const days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let cnt = 0;
    let a = 1;
    let b = 1;

    while (a !== x || b !== y) {
        b++;
        if (b > days[a]) {
            a++;
            b = 1;
        }
        cnt++;
    }
    
    const weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"];
    console.log(weekday[cnt % 7]);
});
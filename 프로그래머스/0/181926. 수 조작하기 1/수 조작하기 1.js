const solution = (n, control) => {
    const cmd = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    var answer = n;
    for (let i = 0; i < control.length; i++) {
        answer += cmd[control[i]];
    }
    return answer;
};
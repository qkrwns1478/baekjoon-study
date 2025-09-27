function solution(str1, str2) {
    var answer = '';
    const n = str1.length;
    for (let i = 0; i < n; i++) {
        answer += str1[i] + str2[i];
    }
    return answer;
}
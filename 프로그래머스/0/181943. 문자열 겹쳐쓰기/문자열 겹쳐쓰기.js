function solution(my_string, overwrite_string, s) {
    let msl = my_string.length;
    let osl = overwrite_string.length;
    let answer = my_string.slice(0, s) + overwrite_string + my_string.slice(s+osl, msl);
    return answer;
}
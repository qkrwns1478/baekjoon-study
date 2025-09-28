function solution(ineq, eq, n, m) {
    if (eq === "=") {
        if (ineq === "<") {
            return Number(n <= m);
        } else {
            return Number(n >= m);
        }
    } else {
        if (ineq === "<") {
            return Number(n < m);
        } else {
            return Number(n > m);
        }
    }
}
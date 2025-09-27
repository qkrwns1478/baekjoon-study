const solution = (a, b, c) => {
    const calc = (a, b, c, i=1) => (a**i + b**i + c**i);
    if (a == b && b == c) {
        return calc(a, b, c) * calc(a, b, c, 2) * calc(a, b, c, 3);
    } else if (a != b && b != c && c != a) {
        return calc(a, b, c);
    } else {
        return calc(a, b, c) * calc(a, b, c, 2);
    }
};
const solution = (a, b) => {
    let a_b = Number(a + "" + b);
    let b_a = Number(b + "" + a);
    return Math.max(a_b, b_a);
};
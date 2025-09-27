const xor = (a, b) => Number(a + "" + b);
const mul = (a, b) => 2 * a * b;
const solution = (a, b) => Math.max(xor(a, b), mul(a, b));
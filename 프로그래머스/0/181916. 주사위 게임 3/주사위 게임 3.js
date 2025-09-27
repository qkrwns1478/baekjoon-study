const solution = (a, b, c, d) => {
    const nums = {};
    for (let i of [a, b, c, d]) {
        nums[i] = (nums[i] || 0) + 1;
    }

    const uniqueCount = Object.keys(nums).length;
    if (uniqueCount == 1) {
        return 1111 * a;
    } else if (uniqueCount == 4) {
        return Math.min(a, b, c, d);
    } else if (uniqueCount == 2) {
        const keys = Object.keys(nums).map(Number);
        let p = keys[0];
        let q = keys[1];

        if (nums[p] == nums[q]) {
            return (p + q) * Math.abs(p - q);
        } else {
            if (nums[p] == 1) {
                [p, q] = [q, p];
            }
            return Math.pow(10 * p + q, 2);
        }
    } else {
        const keys = Object.keys(nums).map(Number);
        let x = keys[0];
        let y = keys[1];
        let z = keys[2];

        let q_val, r_val;
        if (nums[x] == 2) {
            q_val = y;
            r_val = z;
        } else if (nums[y] == 2) {
            q_val = x;
            r_val = z;
        } else {
            q_val = x;
            r_val = y;
        }
        return q_val * r_val;
    }
};